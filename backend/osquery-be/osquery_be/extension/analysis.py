from osquery_be.extension.schemas import (
    AnalysisRequest,
    AnalysisResponse,
    AnalysisResponseData,
)
from osquery_be.extension.url_analysis import get_prediction_from_url


def get_analysis(
    analysis_req: AnalysisRequest,
) -> AnalysisResponse:
    verdict = get_prediction_from_url(analysis_req.url)
    analysis_res = AnalysisResponseData(
        requestId=analysis_req.request_id,
        extensionId=analysis_req.extension_id,
        verdict=verdict,
    )
    return AnalysisResponse(data=analysis_res)
