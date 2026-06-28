from abc import ABC, abstractmethod
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from osef.sdk.capabilities import PluginCapabilities
from osef.sdk.context import ExtensionContext


class PluginQualityTier(str, Enum):
    TIER_1_OFFICIAL = "tier_1_official"
    TIER_2_CERTIFIED = "tier_2_certified"
    TIER_3_COMMUNITY = "tier_3_community"
    EXPERIMENTAL = "experimental"


class PluginCertificationStatus(str, Enum):
    NOT_TESTED = "not_tested"
    VALIDATED = "validated"
    CERTIFIED = "certified"
    REFERENCE = "reference"
    DEPRECATED = "deprecated"


class PluginCertification(BaseModel):
    status: PluginCertificationStatus = PluginCertificationStatus.NOT_TESTED
    certified_against_sdk: Optional[str] = None
    certified_graph_schema: Optional[str] = None
    certified_profiles: List[str] = Field(default_factory=list)
    certification_date: Optional[str] = None
    certification_version: Optional[str] = None


class KnowledgeDomainManifest(BaseModel):
    """Manifest describing a Knowledge Domain."""

    name: str
    version: str
    node_types: List[str] = Field(default_factory=list)
    edge_types: List[str] = Field(default_factory=list)
    adapters: List[str] = Field(default_factory=list)
    projections: List[str] = Field(default_factory=list)
    dashboards: List[str] = Field(default_factory=list)
    policy_packs: List[str] = Field(default_factory=list)


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
    knowledge_domain: Optional[KnowledgeDomainManifest] = None
    quality_tier: PluginQualityTier = PluginQualityTier.EXPERIMENTAL
    supported_profiles: List[str] = Field(default_factory=list)
    certification: PluginCertification = Field(default_factory=PluginCertification)
    
    # Marketplace Metadata
    publisher: Optional[str] = None
    license: Optional[str] = None
    homepage: Optional[str] = None
    repository: Optional[str] = None
    documentation: Optional[str] = None
    keywords: List[str] = Field(default_factory=list)


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
