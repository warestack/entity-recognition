from typing import Any

from pydantic_settings import BaseSettings

from src.constants import Environment


class Config(BaseSettings):
    """
    Configuration class for the application.
    """

    SITE_DOMAIN: str = "myapp.com"

    ENVIRONMENT: Environment = Environment.PRODUCTION

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1"


# Load the configuration
settings = Config()

# FastAPI app configurations
app_configs: dict[str, Any] = {
    "title": "ERS",
    "description": "A FastAPI app designed for technology entity recognition",
}

if settings.ENVIRONMENT.is_deployed:
    app_configs["root_path"] = f"/v{settings.APP_VERSION}"

# Hide OpenAPI docs in production
if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
