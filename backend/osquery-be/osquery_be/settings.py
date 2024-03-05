from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PB_API_URL: str =  "http://localhost:8090/api"
    PB_SERVICE_TOKEN: str = "osquery-be"
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
# settings = Settings(_env_file='prod.env', _env_file_encoding='utf-8')
settings = Settings()