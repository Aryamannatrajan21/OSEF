from typing import Any
from osef_visualization.ir import ProjectedGraph
from osef_visualization.renderers.base import Renderer
from osef_visualization.registries import RendererRegistry

class JsonRenderer(Renderer):
    def get_format(self) -> str:
        return "json"

    def render(self, graph: ProjectedGraph, **kwargs: Any) -> str:
        return graph.model_dump_json(indent=2)

RendererRegistry.register("json", JsonRenderer)
