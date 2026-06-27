from typing import Any
from osef.core.ekg import GraphDelta
from osef_infrastructure.adapters.base import InfrastructureAdapter

class PulumiAdapter(InfrastructureAdapter):
    def parse(self, root_dir: str, **kwargs: Any) -> GraphDelta:
        return GraphDelta()
