from fastapi import APIRouter
from osquery_be.extension.analysis import get_analysis
from osquery_be.extension.schemas import AnalysisRequest, AnalysisResponse

router = APIRouter(prefix="/extension", tags=["extension"])


@router.get("/ping")
async def extensions_ping():
    return "OK"


@router.post("/analysis", response_model=AnalysisResponse)
async def analysis(analysis_req: AnalysisRequest):
    return get_analysis(analysis_req)
