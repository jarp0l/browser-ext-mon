from osquery_be.extension.schemas import (
    AnalysisRequest,
    AnalysisResponse,
    AnalysisResponseData,
    AnalysisVerdict,
)

from random import randint, choice

reasons = ("malware", "phishing", "adware", "tracking", "unknown", "other")


def get_analysis(
    analysis_req: AnalysisRequest,
) -> AnalysisResponse:
    verdict = AnalysisVerdict.GOOD if randint(0, 3) == 0 else AnalysisVerdict.BAD
    reason = "" if verdict == AnalysisVerdict.GOOD else choice(reasons)
    analysis_result = AnalysisResponseData(
        requestId=analysis_req.request_id, extensionId=analysis_req.extension_id, verdict=verdict, reason=reason
    )
    return AnalysisResponse(data=analysis_result)
