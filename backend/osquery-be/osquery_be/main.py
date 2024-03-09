from fastapi import FastAPI

from osquery_be.extension.api import router as extension_router
from osquery_be.osquery.api import router as osquery_router

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/healthz")
async def get_health():
    return "OK"


app.include_router(osquery_router)
app.include_router(extension_router)
