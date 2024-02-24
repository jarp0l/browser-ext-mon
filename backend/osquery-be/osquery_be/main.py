import json

from fastapi import FastAPI, Request

import osquery_be.constants as constants

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/enroll")
async def enroll(req: Request):
    print(await req.json())
    return constants.ENROLL_RESPONSE


@app.get("/config")
async def get_config(req: Request):
    try:
        print(await req.json())
    except json.decoder.JSONDecodeError:
        print(req)
    return constants.EXAMPLE_NODE_CONFIG


@app.post("/config")
async def post_config(req: Request):
    print(await req.json())
    return constants.EXAMPLE_CONFIG


@app.post("/logger")
async def logger(req: Request):
    print(await req.json())
    return {}
