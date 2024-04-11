<template>
  <!-- <section class="section" v-if="apiKey === null"> -->
  <section class="section">
    <div class="columns">
      <div class="column"></div>
      <div class="column is-half">
        <div class="notification is-success" v-if="apiKeyNotif">
          API Key has been set!
        </div>
        <div v-else>
          <div class="field">
            <label class="label">Enter API Key</label>
            <div class="control">
              <input
                class="input"
                type="text"
                placeholder="API Key"
                v-model="apiKey" />
            </div>
            <p class="help">Please enter your organization API key</p>
          </div>
          <div class="control">
            <button class="button is-link" @click="setApiKey">Submit</button>
          </div>
        </div>
      </div>
      <div class="column"></div>
    </div>
  </section>

  <section class="section">
    <div class="columns">
      <div class="column is-one-quarter" id="sidebar">
        <aside class="panel is-danger">
          <p class="panel-heading has-text-centered">BEM Security</p>
          <div class="panel-block">
            <p class="control has-icons-left">
              <input class="input is-danger" type="text" placeholder="Search" />
              <span class="icon is-left">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="16"
                  width="16"
                  viewBox="0 0 512 512">
                  <!-- !Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                  <path
                    d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z" />
                </svg>
              </span>
            </p>
          </div>
          <a class="panel-block" href="#">
            <span class="panel-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                <!-- !Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                <path
                  d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z" />
              </svg>
            </span>
            Overview
          </a>

          <a class="panel-block is-active" href="#installed-extensions">
            <span class="panel-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <!-- !Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                <path
                  d="M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32V274.7l-73.4-73.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l128 128c12.5 12.5 32.8 12.5 45.3 0l128-128c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L288 274.7V32zM64 352c-35.3 0-64 28.7-64 64v32c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V416c0-35.3-28.7-64-64-64H346.5l-45.3 45.3c-25 25-65.5 25-90.5 0L165.5 352H64zm368 56a24 24 0 1 1 0 48 24 24 0 1 1 0-48z" />
              </svg>
            </span>
            Installed Extensions
          </a>

          <a class="panel-block" href="#network-traffic-log">
            <span class="panel-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <!-- !Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
                <path
                  d="M352 256c0 22.2-1.2 43.6-3.3 64H163.3c-2.2-20.4-3.3-41.8-3.3-64s1.2-43.6 3.3-64H348.7c2.2 20.4 3.3 41.8 3.3 64zm28.8-64H503.9c5.3 20.5 8.1 41.9 8.1 64s-2.8 43.5-8.1 64H380.8c2.1-20.6 3.2-42 3.2-64s-1.1-43.4-3.2-64zm112.6-32H376.7c-10-63.9-29.8-117.4-55.3-151.6c78.3 20.7 142 77.5 171.9 151.6zm-149.1 0H167.7c6.1-36.4 15.5-68.6 27-94.7c10.5-23.6 22.2-40.7 33.5-51.5C239.4 3.2 248.7 0 256 0s16.6 3.2 27.8 13.8c11.3 10.8 23 27.9 33.5 51.5c11.6 26 20.9 58.2 27 94.7zm-209 0H18.6C48.6 85.9 112.2 29.1 190.6 8.4C165.1 42.6 145.3 96.1 135.3 160zM8.1 192H131.2c-2.1 20.6-3.2 42-3.2 64s1.1 43.4 3.2 64H8.1C2.8 299.5 0 278.1 0 256s2.8-43.5 8.1-64zM194.7 446.6c-11.6-26-20.9-58.2-27-94.6H344.3c-6.1 36.4-15.5 68.6-27 94.6c-10.5 23.6-22.2 40.7-33.5 51.5C272.6 508.8 263.3 512 256 512s-16.6-3.2-27.8-13.8c-11.3-10.8-23-27.9-33.5-51.5zM135.3 352c10 63.9 29.8 117.4 55.3 151.6C112.2 482.9 48.6 426.1 18.6 352H135.3zm358.1 0c-30 74.1-93.6 130.9-171.9 151.6c25.5-34.2 45.2-87.7 55.3-151.6H493.4z" />
              </svg>
            </span>
            Network Traffic Log
          </a>
        </aside>
      </div>

      <div class="column" id="overview">
        <div class="card" id="statistics">
          <div class="card-content">
            <nav class="level">
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Total Extensions</p>
                  <p class="title">{{ extensions.length }}</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Total requests</p>
                  <p class="title">
                    {{ statsCount.malicious + statsCount.safe }}
                  </p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Allowed</p>
                  <p class="title">{{ statsCount.safe }}</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Blocked</p>
                  <p class="title">{{ statsCount.malicious }}</p>
                </div>
              </div>
            </nav>
          </div>
        </div>

        <section class="section" id="installed-extensions">
          <h1 class="title">Installed Extensions</h1>
          <ag-grid-vue
            :rowData="extensions"
            :columnDefs="extensionColDefs"
            :gridOptions="gridOptions"
            style="height: 500px"
            class="ag-theme-quartz">
          </ag-grid-vue>
        </section>

        <section class="section" id="network-traffic-log">
          <h1 class="title">Network Traffic Log</h1>
          <ag-grid-vue
            :rowData="extensionLogs"
            :columnDefs="extensionLogColDefs"
            :gridOptions="gridOptions"
            style="height: 500px"
            class="ag-theme-quartz">
          </ag-grid-vue>
        </section>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import "ag-grid-community/styles/ag-grid.css"
import "ag-grid-community/styles/ag-theme-quartz.css"
import "~main.css"

import { watch } from "fs"
import type { GridOptions } from "ag-grid-community"
import { AgGridVue } from "ag-grid-vue3"
import { onMounted, ref, watchEffect, type Ref } from "vue"


import type { Extension, ExtensionLog } from "~utils/interfaces"
import { AnalysisVerdict } from "~utils/interfaces"

const extensions: Ref<Extension[]> = ref([])
const extensionLogs: Ref<ExtensionLog[]> = ref([])
const statsCount = ref({ safe: 0, malicious: 0 })

const extensionColDefs = ref([
  { field: "id" },
  { field: "name" },
  { field: "description" }
])

const extensionLogColDefs = ref([
  { field: "extension" },
  // { field: "id" },
  { field: "url" },
  { field: "method" },
  { field: "resourceType" },
  { field: "verdict" }
])

const gridOptions: GridOptions = {
  autoSizeStrategy: { type: "fitCellContents" },
  defaultColDef: {
    filter: "agTextColumnFilter",
    floatingFilter: true
  },
  pagination: true,
  paginationPageSize: 25,
  paginationPageSizeSelector: [25, 50, 75, 100, 125, 150, 175, 200]
}

const apiKey = ref(null)
const apiKeyNotif = ref(false)

// const setApiKey = async (key) => {
//   await storage.set("apiKey", key)
// }

onMounted(async () => {
  extensions.value = await getExtensions()

  chrome.storage.local.get((s) => {
    console.warn(s)
    extensionLogs.value = s?.extensionLogs || []
    apiKey.value = s?.apiKey || null
  })

  statsCount.value = countRequests(extensionLogs.value)
})

watchEffect(() => {
  chrome.storage.onChanged.addListener((changes, namespace) => {
    if (namespace === "local" && changes.extensionLogs) {
      extensionLogs.value = changes.extensionLogs.newValue || []
    }
  })
})

watchEffect(() => {
  statsCount.value = countRequests(extensionLogs.value)
})

function countRequests(logs: ExtensionLog[]): {
  safe: number
  malicious: number
} {
  let safeCount = 0
  let maliciousCount = 0

  for (const log of logs) {
    if (log.verdict === AnalysisVerdict.SAFE) {
      safeCount++
    } else if (
      log.verdict === AnalysisVerdict.MALWARE ||
      log.verdict === AnalysisVerdict.PHISHING ||
      log.verdict === AnalysisVerdict.DEFACEMENT
    ) {
      maliciousCount++
    }
  }

  return { safe: safeCount, malicious: maliciousCount }
}

async function getExtensions(): Promise<Extension[]> {
  const exts: Extension[] = []
  const hasPerm = await chrome.permissions.contains({
    permissions: ["management"]
  })
  if (!hasPerm) return []
  const extInfo = await chrome.management.getAll()
  for (let { id, name, description } of extInfo) {
    const extension: Extension = {
      id,
      name,
      description
      // icon: icons?.[icons?.length - 1]?.url,
    }
    exts.push(extension)
  }
  return exts
}

let apiBaseUrl = "http://localhost:1337"

async function checkApiKey(req) {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      apiKey: req.apiKey
    })
  }

  try {
    const res = await fetch(`${apiBaseUrl}/extension/apikey`, options)
    if (!res.ok) {
      throw new Error(`HTTP error! Status: ${res.status}`)
    }
    const { data } = await res.json()
    return data
  } catch (err) {
    console.error(err)
    return null
  }
}

function setApiKey() {
  console.log("Setting API Key")
  console.log(apiKey.value)

  const apiKeyResult = checkApiKey({
    apiKey: apiKey.value
  })
  if (apiKeyResult) {
    // storage.set("apiKey", apiKey.value)
    chrome.storage.local.set({ apiKey: apiKey.value })
    apiKeyNotif.value = true
  }
}
</script>
