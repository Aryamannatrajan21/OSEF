import logging
from typing import Dict, List, Optional, Type, Any
from osef.sdk.capabilities import CapabilityDescriptor, ParserCapability, GraphEnrichmentCapability, PolicyCapability

logger = logging.getLogger(__name__)

class CapabilityRegistry:
    """
    Internal registry that owns capability registration, language matching,
    priority resolution, and conflict detection.
    """
    def __init__(self):
        # We store capabilities by descriptor type.
        self._capabilities: Dict[Type[CapabilityDescriptor], List[CapabilityDescriptor]] = {
            ParserCapability: [],
            GraphEnrichmentCapability: []
        }
        self._plugin_mapping: Dict[CapabilityDescriptor, str] = {} # capability -> plugin id

    def register(self, capability: CapabilityDescriptor, plugin_id: str) -> None:
        """Register a runtime capability from a plugin."""
        cap_type = type(capability)
        if cap_type not in self._capabilities:
            self._capabilities[cap_type] = []
            
        self._capabilities[cap_type].append(capability)
        self._plugin_mapping[capability] = plugin_id
        
        name = getattr(capability, 'name', getattr(capability, 'language', 'unknown'))
        logger.info(f"Registered {cap_type.__name__}: {name} (from {plugin_id})")

    def resolve_parser(self, language: str) -> Optional[ParserCapability]:
        """
        Resolution Algorithm:
        - Match Language
        - (Future) Priority/Ranking Score
        """
        candidates = [
            c for c in self._capabilities[ParserCapability] 
            if isinstance(c, ParserCapability) and c.language == language
        ]
        
        if not candidates:
            return None
            
        return candidates[0]
        
    def get_enrichers(self) -> List[GraphEnrichmentCapability]:
        """Returns all registered graph enrichment capabilities."""
        return [c for c in self._capabilities.get(GraphEnrichmentCapability, []) if isinstance(c, GraphEnrichmentCapability)]

    def get_policies(self) -> List[Any]:
        """Returns all registered policy rules from plugins."""
        policies = []
        for cap in self._capabilities.get(PolicyCapability, []):
            if isinstance(cap, PolicyCapability):
                policies.extend(cap.factory())
        return policies
