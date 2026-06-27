from typing import Any
from osef.core.ekg import GraphDelta
from .akm import AKM

class BaseArchitectureAdapter:
    def parse(self, filepath: str) -> GraphDelta:
        raise NotImplementedError

class C4ModelAdapter(BaseArchitectureAdapter):
    def parse(self, filepath: str) -> GraphDelta:
        delta = GraphDelta()
        comp = AKM.create_node(
            type_name=AKM.COMPONENT.value,
            name="MockedC4Component",
            source_adapter="C4ModelAdapter",
            metadata={"technology": "Python"}
        )
        delta.nodes_to_add.append(comp)
        return delta

class OsefArchitectureAdapter(BaseArchitectureAdapter):
    def parse(self, filepath: str) -> GraphDelta:
        delta = GraphDelta()
        layer = AKM.create_node(
            type_name=AKM.LAYER.value,
            name="MockedLayer",
            source_adapter="OsefArchitectureAdapter",
            metadata={"description": "Core Logic"}
        )
        delta.nodes_to_add.append(layer)
        return delta

class ADRAdapter(BaseArchitectureAdapter):
    def parse(self, filepath: str) -> GraphDelta:
        delta = GraphDelta()
        decision = AKM.create_node(
            type_name=AKM.DECISION.value,
            name="MockedDecision",
            source_adapter="ADRAdapter",
            metadata={"status": "Accepted"}
        )
        delta.nodes_to_add.append(decision)
        return delta

class StructurizrAdapter(BaseArchitectureAdapter):
    def parse(self, filepath: str) -> GraphDelta:
        pass

class PlantUMLAdapter(BaseArchitectureAdapter):
    def parse(self, filepath: str) -> GraphDelta:
        pass

class ArchiMateAdapter(BaseArchitectureAdapter):
    def parse(self, filepath: str) -> GraphDelta:
        pass
