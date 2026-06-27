from typing import Any
from osef_visualization.ir import ProjectedGraph
from osef_visualization.renderers.base import Renderer
from osef_visualization.registries import RendererRegistry

class HtmlRenderer(Renderer):
    def get_format(self) -> str:
        return "html"

    def render(self, graph: ProjectedGraph, **kwargs: Any) -> str:
        raise NotImplementedError("Interactive HTML rendering is scheduled for Version 2 of the Visualization Plugin.")

RendererRegistry.register("html", HtmlRenderer)
