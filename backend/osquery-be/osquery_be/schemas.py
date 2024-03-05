from pydantic import BaseModel

#  class OSVersion(BaseModel):
#      arch: str
#      build: str
     

#  class HostDetails(BaseModel):
     
    

class EnrollRequestSchema(BaseModel):
    enroll_secret: str
    host_identifier: str
    platform_type: str
    host_details: dict
    