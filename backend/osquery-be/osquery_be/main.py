import json

from fastapi import FastAPI, Request

import osquery_be.constants as constants
from osquery_be.schemas import EnrollRequest, EnrollResponse
from osquery_be.utils.enroll import enroll_node

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


@app.get("/osquery/config")
async def get_config(req: Request):
    try:
        print(await req.json())
    except json.decoder.JSONDecodeError:
        print(req)
    return constants.EXAMPLE_NODE_CONFIG


@app.post("/osquery/config")
async def post_config(req: Request):
    print(await req.json())
    return constants.EXAMPLE_CONFIG


@app.post("/osquery/logger")
async def logger(req: Request):
    print(await req.json())
    return {}
