from pydantic import BaseModel
from typing import Optional


class Capability(BaseModel):
    name: str
    version: str


class PluginCapabilities(BaseModel):
    provides_parser: Optional[Capability] = None
    provides_semantic_enrichment: Optional[Capability] = None
    provides_rule_packs: Optional[Capability] = None
    provides_reports: Optional[Capability] = None
    provides_cli_commands: Optional[Capability] = None
    supports_sdk: Capability
    supports_graph_schema: Capability


from typing import Callable, Any, TYPE_CHECKING, List

if TYPE_CHECKING:
    from osef.core.ekg import KnowledgeGraph, GraphDelta
    from osef.sdk.pipeline import PipelineContext
    from osef.parser.symbol_table import SymbolTable

class CapabilityDescriptor:
    """Base runtime capability descriptor for plugins."""
    def __init__(self, stage: str = "default", priority: int = 100, 
                 dependencies: List[str] = None, produces: List[str] = None):
        self.stage = stage
        self.priority = priority
        self.dependencies = dependencies or []
        self.produces = produces or []

class ParserCapability(CapabilityDescriptor):
    def __init__(self, language: str, factory: Callable[['PipelineContext'], 'SymbolTable'], **kwargs):
        super().__init__(**kwargs)
        self.language = language
        self.factory = factory

class GraphEnrichmentCapability(CapabilityDescriptor):
    def __init__(self, name: str, factory: Callable[['PipelineContext', 'KnowledgeGraph'], 'GraphDelta'], **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.factory = factory

class PolicyCapability(CapabilityDescriptor):
    def __init__(self, name: str, factory: Callable[[], List[Any]], **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.factory = factory

class CLIExtensionCapability(CapabilityDescriptor):
    def __init__(self, command_name: str, factory: Callable, **kwargs):
        super().__init__(**kwargs)
        self.command_name = command_name
        self.factory = factory

class ReportCapability(CapabilityDescriptor):
    def __init__(self, name: str, factory: Callable, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.factory = factory
