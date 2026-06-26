from abc import ABC, abstractmethod
from typing import Optional
from pydantic import BaseModel
from osef.sdk.capabilities import PluginCapabilities
from osef.sdk.context import ExtensionContext


class PluginManifest(BaseModel):
    id: str
    name: str
    description: str
    version: str
    author: str
    license: str
    homepage: Optional[str] = None
    signature: Optional[str] = None
    checksum: Optional[str] = None
    capabilities: PluginCapabilities


class OsefPlugin(ABC):
    @property
    @abstractmethod
    def manifest(self) -> PluginManifest:
        pass

    @abstractmethod
    def activate(self, context: ExtensionContext) -> None:
        pass

    @abstractmethod
    def deactivate(self) -> None:
        pass
