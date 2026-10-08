from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "code-review-agent"
    log_level: str = "INFO"

    github_webhook_secret: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()    
    