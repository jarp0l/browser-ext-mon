let requests: object = {}
let needSave: boolean = false
// let muted: boolean = false;
let blocked: boolean = false
let blockedExtUrls: object = {}
let extRuleIds: object = {}
let recycleRuleIds = []
let maxRuleId = 1
let allRuleIds = [1]

let apiBaseUrl = "http://localhost:1337"

interface AnalysisRequest {
  reqMethod: string
  reqUrl: string
  resourceType: string
  reqId: string
  extensionId: string
}

interface AnalysisResponse {
  data: {
    requestId: string
    extensionId: string
    verdict: AnalysisVerdict
    reason: string
  }
}

enum AnalysisVerdict {
  GOOD = "good",
  BAD = "bad"
}

chrome.storage.local.get((s) => {
  // muted = s?.muted || {}
  blocked = s?.blocked || {}
  extRuleIds = s?.extRuleIds || {}
  recycleRuleIds = s?.recycleRuleIds || []
  maxRuleId = s?.maxRuleId || 1
  allRuleIds = s?.allRuleIds || [1]
  blockedExtUrls = s?.blockedExtUrls || {}
  requests = s?.requests || {}
})

/**
 * Get whether the browser is brave or another chrome browser
 *
 * @returns "brave" or "chrome"
 */
const getBrowserType = () => ("brave" in navigator ? "brave" : "chrome")

/**
 * Check whether the extension is the current/calling extension
 *
 * @param extensionId Id of the extension to check
 * @returns `true` if the extension is the current extension, `false` otherwise
 */
async function isCurrentExtension(extensionId: string): Promise<boolean> {
  return new Promise((resolve) => {
    chrome.management.getSelf((info) => {
      resolve(info.id === extensionId)
    })
  })
}

async function performAnalysis(
  req: AnalysisRequest
): Promise<AnalysisResponse["data"]> | null {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      method: req.reqMethod,
      url: req.reqUrl,
      resourceType: req.resourceType,
      requestId: req.reqId,
      extensionId: req.extensionId
    })
  }

  try {
    const res = await fetch(`${apiBaseUrl}/extension/analysis`, options)
    if (!res.ok) {
      throw new Error(`HTTP error! Status: ${res.status}`)
    }
    const { data } = (await res.json()) as AnalysisResponse
    return data
  } catch (err) {
    console.error(err)
    return null
  }
}

async function setupListener() {
  const hasPerm = await chrome.permissions.contains({
    permissions: ["declarativeNetRequestFeedback"]
  })
  if (!hasPerm) return

  // We need `onRuleMatchedDebug` to track the number of requests and notify the user.
  // But `declarativeNetRequest.onRuleMatchedDebug` API is only available in debug mode.
  if (!chrome.declarativeNetRequest?.onRuleMatchedDebug) return

  chrome.declarativeNetRequest.onRuleMatchedDebug.addListener(async (e) => {
    if (e.request.initiator?.startsWith("chrome-extension://")) {
      const extensionId = e.request.initiator.replace("chrome-extension://", "")

      if (await isCurrentExtension(extensionId)) {
        return
      }

      const analysisResult = await performAnalysis({
        reqMethod: e.request.method,
        reqUrl: e.request.url,
        resourceType: e.request.type,
        reqId: e.request.requestId,
        extensionId
      })

      if (
        analysisResult !== null &&
        analysisResult.verdict === AnalysisVerdict.BAD
      ) {
        console.log(`Blocking request from ${extensionId} to ${e.request.url}`)
      }

      if (!requests[extensionId]) {
        requests[extensionId] = {
          reqUrls: {},
          numRequestsAllowed: 0,
          numRequestsBlocked: 0
        }
      }

      const req = requests[extensionId]
      const url = [e.request.method, e.request.url].filter(Boolean).join(" ")
      req.numRequestsAllowed = req.numRequestsAllowed || 0
      req.numRequestsBlocked = req.numRequestsBlocked || 0

      if (!req.reqUrls[url] || typeof req.reqUrls[url] !== "object") {
        req.reqUrls[url] = {
          blocked: 0,
          allowed: typeof req.reqUrls[url] === "number" ? req.reqUrls[url] : 0
        }
      }

      if (allRuleIds.includes(e.rule.ruleId)) {
        req.numRequestsBlocked += 1
        req.reqUrls[url].blocked += 1
      } else {
        req.numRequestsAllowed += 1
        req.reqUrls[url].allowed += 1
      }
      const urlObj = new URL(e.request.url)
      const blockedUrl = [urlObj.protocol, "//", urlObj.host, urlObj.pathname]
        .filter(Boolean)
        .join("")
      req.reqUrls[url].isBlocked =
        blockedExtUrls[extensionId]?.[blockedUrl] || false
    }
  })
}

async function getExtensions() {
  const extensions = {}
  const hasPerm = await chrome.permissions.contains({
    permissions: ["management"]
  })
  if (!hasPerm) return []
  const extInfo = await chrome.management.getAll()
  for (let { enabled, name, id, icons } of extInfo) {
    extensions[id] = {
      name,
      id,
      numRequestsAllowed: 0,
      numRequestsBlocked: 0,
      reqUrls: {},
      icon: icons?.[icons?.length - 1]?.url,
      blocked: blocked[id],
      // muted: muted[id],
      enabled,
      ...(requests[id] || {})
    }
  }
  return extensions
}

getExtensions().then((exts) => {
  console.log(exts)
})

setupListener()
