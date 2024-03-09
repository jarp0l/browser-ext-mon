from fastapi import FastAPI

from osquery_be.extension.analysis import get_analysis
from osquery_be.extension.schemas import (
    AnalysisRequest,
    AnalysisResponse,
)
from osquery_be.osquery.config import get_config
from osquery_be.osquery.enroll import enroll_node
from osquery_be.osquery.logger import store_logs
from osquery_be.schemas.config_schemas import ConfigRequest, ConfigResponse
from osquery_be.schemas.enroll_schemas import EnrollRequest, EnrollResponse
from osquery_be.schemas.logger_schemas import LoggerRequest, LoggerResponse

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/healthz")
async def get_health():
    return "OK"


@app.post("/osquery/enroll", response_model=EnrollResponse)
async def enroll(enroll_req: EnrollRequest):
    res = enroll_node(enroll_req)
    return res


@app.post("/osquery/config", response_model=ConfigResponse)
async def post_config(config_req: ConfigRequest):
    res = get_config(config_req)
    return res


@app.post("/osquery/logger", response_model=LoggerResponse)
async def logger(logger_req: LoggerRequest):
    res = store_logs(logger_req)
    return res


@app.get("/extension/ping")
async def extensions_ping():
    return "OK"


@app.post("/extension/analysis", response_model=AnalysisResponse)
async def analysis(analysis_req: AnalysisRequest):
    return get_analysis(analysis_req)
