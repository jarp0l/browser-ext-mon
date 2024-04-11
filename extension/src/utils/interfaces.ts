export enum AnalysisVerdict {
  SAFE = "safe",
  DEFACEMENT = "defacement",
  PHISHING = "phishing",
  MALWARE = "malware"
}

export enum RequestMethod {
  GET = "GET",
  POST = "POST",
  PUT = "PUT",
  DELETE = "DELETE",
  PATCH = "PATCH"
}

export interface AnalysisRequest {
  reqMethod: string
  reqUrl: string
  resourceType: string
  reqId: string
  extensionId: string
}

export interface AnalysisResponse {
  data: {
    requestId: string
    extensionId: string
    verdict: AnalysisVerdict
  }
}

export interface Extension {
  id: string
  name: string
  description: string
}

export interface ExtensionLog {
  extension: string
  //   id: string
  method: string
  url: string
  resourceType: string
  verdict: AnalysisVerdict
}
