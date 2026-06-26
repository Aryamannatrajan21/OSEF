from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
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
    documentation: Optional[str] = None
    sdk_version: str
    graph_schema: str
    policy_api: str
    capabilities: PluginCapabilities
    dependencies: List[str] = Field(default_factory=list)
    entry_points: Dict[str, str] = Field(default_factory=dict)
    keywords: List[str] = Field(default_factory=list)
    signature: Optional[str] = None
    checksum: Optional[str] = None


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
