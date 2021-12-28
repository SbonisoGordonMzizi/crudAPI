from pydantic import BaseSettings


class ConfigEnv(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_valid_time: str

    class Config:
        env_file = ".env"


config_env = ConfigEnv()
