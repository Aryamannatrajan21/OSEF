"""
Configuration Loader using pydantic-settings.
"""

from typing import Any, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from osef.contracts.providers import ConfigProvider


class OSEFSettings(BaseSettings):
    """
    Core settings for OSEF.
    """

    model_config = SettingsConfigDict(
        env_prefix="OSEF_", env_file=".env", extra="ignore"
    )

    debug: bool = False
    log_level: str = "INFO"
    environment: str = "development"


class DefaultConfigProvider(ConfigProvider):
    """
    Configuration Provider implementing ConfigProvider protocol.
    """

    def __init__(self, settings: Optional[OSEFSettings] = None) -> None:
        self._settings = settings or OSEFSettings()

    def get(self, key: str, default: Any = None) -> Any:
        return getattr(self._settings, key, default)
