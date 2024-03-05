from pydantic import BaseModel


class EnrollRequest(BaseModel):
    enroll_secret: str
    host_identifier: str
    platform_type: str
    host_details: dict


class EnrollResponse(BaseModel):
    node_key: str
