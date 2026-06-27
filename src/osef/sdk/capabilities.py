from pydantic import BaseModel
from typing import Optional, Callable, Any, TYPE_CHECKING, List


class Capability(BaseModel):
    name: str
    version: str


class PluginCapabilities(BaseModel):
    provides_parser: Optional[Capability] = None
    provides_semantic_enrichment: Optional[Capability] = None
    provides_rule_packs: Optional[Capability] = None
    provides_reports: Optional[Capability] = None
    provides_cli_commands: Optional[Capability] = None
    provides_projections: Optional[Capability] = None
    supports_sdk: Capability
    supports_graph_schema: Capability


if TYPE_CHECKING:
    from osef.core.ekg import KnowledgeGraph, GraphDelta
    from osef.sdk.pipeline import PipelineContext
    from osef.parser.symbol_table import SymbolTable


class CapabilityDescriptor:
    """Base runtime capability descriptor for plugins."""

    def __init__(
        self,
        stage: str = "default",
        priority: int = 100,
        dependencies: Optional[List[str]] = None,
        produces: Optional[List[str]] = None,
    ):
        self.stage = stage
        self.priority = priority
        self.dependencies = dependencies or []
        self.produces = produces or []


class ParserCapability(CapabilityDescriptor):
    def __init__(
        self,
        language: str,
        factory: Callable[["PipelineContext"], "SymbolTable"],
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.language = language
        self.factory = factory


class GraphEnrichmentCapability(CapabilityDescriptor):
    def __init__(
        self,
        name: str,
        factory: Callable[["PipelineContext", "KnowledgeGraph"], "GraphDelta"],
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.name = name
        self.factory = factory


class PolicyCapability(CapabilityDescriptor):
    def __init__(self, name: str, factory: Callable[[], List[Any]], **kwargs: Any):
        super().__init__(**kwargs)
        self.name = name
        self.factory = factory


class CLIExtensionCapability(CapabilityDescriptor):
    def __init__(self, command_name: str, factory: Callable[..., Any], **kwargs: Any):
        super().__init__(**kwargs)
        self.command_name = command_name
        self.factory = factory


class ReportCapability(CapabilityDescriptor):
    def __init__(self, name: str, factory: Callable[..., Any], **kwargs: Any):
        super().__init__(**kwargs)
        self.name = name
        self.factory = factory


class ProjectionCapability(CapabilityDescriptor):
    def __init__(self, name: str, factory: Callable[..., Any], **kwargs: Any):
        super().__init__(**kwargs)
        self.name = name
        self.factory = factory
