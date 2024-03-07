from typing import Annotated

from pydantic import BaseModel, EmailStr


class EnrollSecret(BaseModel):
    api_key: str
    owner_email: Annotated[EmailStr | str, "owner_email is optional"] = ""

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"api_key": "jeI4IHLEx8mEoYd5", "owner_email": "abc@example.com"},
                {"api_key": "jeI4IHLEx8mEoYd5", "owner_email": ""},
            ]
        }
    }


class EnrollRequest(BaseModel):
    enroll_secret: Annotated[str, "Raw json with the structure of EnrollSecret"]
    host_identifier: str
    platform_type: str
    host_details: dict

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "enroll_secret": '{\n  "api_key": "jeI4IHLEx8mEoYd5",\n  "owner_email": "abc@example.com"\n}',
                    "host_identifier": "6d0481b2-fd6d-435f-80bc-564a8736dd56",
                    "platform_type": "21",
                    "host_details": {},
                },
                {
                    "enroll_secret": '{\n  "api_key": "jeI4IHLEx8mEoYd5",\n  "owner_email": ""\n}',
                    "host_identifier": "6d0481b2-fd6d-435f-80bc-564a8736dd56",
                    "platform_type": "21",
                    "host_details": {},
                },
            ]
        }
    }


class EnrollResponse(BaseModel):
    node_key: str = ""
    node_invalid: bool = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "node_key": "6d0481b2-fd6d-435f-80bc-564a8736dd56",
                    "node_invalid": False,
                },
                {
                    "node_key": "",
                    "node_invalid": True,
                },
            ]
        }
    }
