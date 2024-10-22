from enum import Enum

from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    method: str
    url: str
    resource_type: str = Field(..., alias="resourceType")
    request_id: str = Field(..., alias="requestId")
    extension_id: str = Field(..., alias="extensionId")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "method": "GET",
                    "url": "https://example.com",
                    "resourceType": "xmlhttprequest",
                    "requestId": "1",
                    "extensionId": "fjlkfpfpajiaobkbonlafhkncagkdogj",
                },
                {
                    "method": "POST",
                    "url": "https://example.com/users",
                    "resourceType": "xmlhttprequest",
                    "requestId": "2",
                    "extensionId": "fjlkfpfpajiaobkbonlafhkncagkdogj",
                },
            ]
        }
    }


class AnalysisVerdict(str, Enum):
    SAFE = "safe"
    DEFACEMENT = "defacement"
    PHISHING = "phishing"
    MALWARE = "malware"


class AnalysisResponseData(BaseModel):
    request_id: str = Field(..., alias="requestId")
    extension_id: str = Field(..., alias="extensionId")
    verdict: AnalysisVerdict


class AnalysisResponse(BaseModel):
    data: AnalysisResponseData

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "data": {
                        "requestId": "1",
                        "extensionId": "fjlkfpfpajiaobkbonlafhkncagkdogj",
                        "verdict": "safe",
                    }
                },
                {
                    "data": {
                        "requestId": "2",
                        "extensionId": "fjlkfpfpajiaobkbonlafhkncagkdogj",
                        "verdict": "phishing",
                    }
                },
            ]
        }
    }
