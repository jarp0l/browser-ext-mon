from fastapi import APIRouter

from osquery_be.osquery.config import get_config
from osquery_be.osquery.enroll import enroll_node
from osquery_be.osquery.logger import store_logs
from osquery_be.osquery.schemas.config_schemas import ConfigRequest, ConfigResponse
from osquery_be.osquery.schemas.enroll_schemas import EnrollRequest, EnrollResponse
from osquery_be.osquery.schemas.logger_schemas import LoggerRequest, LoggerResponse

router = APIRouter(prefix="/osquery", tags=["osquery"])


@router.post("/enroll", response_model=EnrollResponse)
async def enroll(enroll_req: EnrollRequest):
    res = enroll_node(enroll_req)
    return res


@router.post("/config", response_model=ConfigResponse)
async def post_config(config_req: ConfigRequest):
    res = get_config(config_req)
    return res


@router.post("/logger", response_model=LoggerResponse)
async def logger(logger_req: LoggerRequest):
    res = store_logs(logger_req)
    return res
