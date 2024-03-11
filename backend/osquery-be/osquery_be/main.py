import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI

from osquery_be.extension.api import router as extension_router
from osquery_be.extension.model_loader import ModelLoader
from osquery_be.osquery.api import router as osquery_router
from osquery_be.settings import settings

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    logging.info("")
    logging.info(">>> Loading models...")
    start_time = time.time()
    model_loader = ModelLoader()
    settings.ml_models["url_analysis"] = model_loader.load_model("url_analysis")
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(
        f">>> Finished loading ML models. Took {execution_time * 1000} milliseconds.\n"
    )
    yield
    # Clean up the ML models and release the resources
    settings.ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/healthz")
async def get_health():
    return "OK"


app.include_router(osquery_router)
app.include_router(extension_router)
