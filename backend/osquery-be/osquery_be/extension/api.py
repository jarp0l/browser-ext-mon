from fastapi import APIRouter
from osquery_be.extension.analysis import get_analysis
from osquery_be.extension.blacklist import get_blacklist
from osquery_be.extension.schemas import (
    AnalysisRequest,
    AnalysisResponse,
    ApiKeyRequest,
)

router = APIRouter(prefix="/extension", tags=["extension"])


@router.get("/ping")
async def extensions_ping():
    return "OK"


@router.post("/analysis", response_model=AnalysisResponse)
async def analysis(analysis_req: AnalysisRequest):
    return get_analysis(analysis_req)


@router.post("/apikey")
async def apikey(api_key_req: ApiKeyRequest):
    print(api_key_req)
    return "apikey"


@router.post("/blacklist")
async def blacklist(api_key_req: ApiKeyRequest):
    return get_blacklist(api_key_req)
