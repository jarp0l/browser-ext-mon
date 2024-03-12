from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for osquery-be.

    The environment variables are automatically read from shell environment or .env file, in that order.
    The alias parameter on Field() is used to read an environment variable with another name.
    Unless case sensitivity is set to True, the environment variables are case insensitive.
    """

    # host.docker.internal is a special DNS name which resolves to the internal IP address used by the host
    # We need this to connect to backen/pb instance running on the host machine
    pb_api_url: str = Field("http://localhost:8090/api", alias="PB_API_DOCKER_URL")
    service_token: str = "osquery-be"
    ml_models: dict = {}

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )


settings = Settings()
