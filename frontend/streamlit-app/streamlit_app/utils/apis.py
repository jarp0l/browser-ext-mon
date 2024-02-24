import logging
import os

import httpx

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8090/api")


def make_request(method, endpoint, data):
    try:
        res = httpx.request(method, f"{API_BASE_URL}{endpoint}", json=data)
        if res.status_code == 200:
            return res.json()
        elif res.status_code in [400, 403]:
            logging.error(res.json())
            return {}
    except Exception as e:
        logging.error(e)
        return {}
