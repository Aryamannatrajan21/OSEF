import logging
from typing import Dict, List, Optional, Type, TypeVar
from osef.sdk.providers import BaseProvider, BaseParserProvider

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseProvider)

class CapabilityRegistry:
    """
    Internal registry that owns provider registration, validation, language matching,
    priority resolution, and conflict detection.
    """
    def __init__(self):
        # We store providers by capability interface.
        self._providers: Dict[Type[BaseProvider], List[BaseProvider]] = {
            BaseParserProvider: []
        }
        self._plugin_mapping: Dict[str, str] = {} # provider name -> plugin id

    def register(self, provider: BaseProvider, plugin_id: str) -> None:
        """Register a provider capability from a plugin."""
        # Detect interface
        if isinstance(provider, BaseParserProvider):
            self._providers[BaseParserProvider].append(provider)
            self._plugin_mapping[provider.name] = plugin_id
            logger.info(f"Registered Parser Provider: {provider.name} v{provider.version} (from {plugin_id})")
        else:
            logger.warning(f"Unknown provider type for {provider.name}")

    def resolve_parser(self, language: str) -> Optional[BaseParserProvider]:
        """
        Resolution Algorithm:
        - Match Language
        - (Future) Priority/Ranking Score
        """
        candidates = [
            p for p in self._providers[BaseParserProvider] 
            if getattr(p, "language", None) == language
        ]
        
        if not candidates:
            return None
            
        # For now, just return the first matched candidate
        # Ranking/Scoring goes here in future iterations
        return candidates[0]
