import logging

import httpx
from osquery_be.osquery.exceptions import InvalidAPIKeyException
from osquery_be.settings import settings


def get_blacklist(api_key_req):
    # first get org_id from api_key_req.api_key
    # then blacklist from org_id

    api_key = api_key_req.api_key

    headers = {
        "X-SERVICE-TOKEN": settings.service_token,
    }

    try:
        client = httpx.Client()

        # Check if the api_key is valid
        search_orgs = client.get(
            f"{settings.pb_api_url}/collections/organizations/records",
            headers=headers,
            params={"filter": f"(api_key='{api_key}')"},
        ).json()

        # If api_key belongs to any organization, totalItems will be 1
        if search_orgs["totalItems"] != 1:
            raise InvalidAPIKeyException

        search_blacklist = client.get(
            f"{settings.pb_api_url}/collections/blacklist/records",
            headers=headers,
            params={"filter": f"(org_id='{search_orgs['items'][0]['id']}')"},
        ).json()

        if search_blacklist["totalItems"] != 1:
            return None

    except Exception as e:
        logging.exception(f"Error: {e}")
        return None
