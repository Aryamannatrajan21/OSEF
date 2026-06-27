from typing import Any
from osef_visualization.ir import ProjectedGraph
from osef_visualization.renderers.base import Renderer
from osef_visualization.registries import RendererRegistry

class GraphvizRenderer(Renderer):
    def get_format(self) -> str:
        return "graphviz"

    def render(self, graph: ProjectedGraph, **kwargs: Any) -> str:
        lines = ['digraph G {']
        lines.append(f'  label="{graph.metadata.name}";')
        lines.append('  node [shape=box, style=filled, color=lightgrey];')
        
        for node in graph.nodes:
            clean_id = f'"{node.id}"'
            shape = "folder" if node.attributes.get("shape") == "folder" else "box"
            lines.append(f'  {clean_id} [label="{node.label}", shape="{shape}"];')
            
        for edge in graph.edges:
            clean_source = f'"{edge.source_id}"'
            clean_target = f'"{edge.target_id}"'
            style = "dashed" if edge.attributes.get("style") == "dashed" else "solid"
            
            label_attr = f', label="{edge.label}"' if edge.label else ""
            lines.append(f'  {clean_source} -> {clean_target} [style="{style}"{label_attr}];')

        lines.append('}')
        return "\n".join(lines)

RendererRegistry.register("graphviz", GraphvizRenderer)
