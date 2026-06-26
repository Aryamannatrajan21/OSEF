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
