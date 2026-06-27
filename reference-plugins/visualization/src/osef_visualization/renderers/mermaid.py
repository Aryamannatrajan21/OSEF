from typing import Any
from osef_visualization.ir import ProjectedGraph
from osef_visualization.renderers.base import Renderer
from osef_visualization.registries import RendererRegistry

class MermaidRenderer(Renderer):
    def get_format(self) -> str:
        return "mermaid"

    def render(self, graph: ProjectedGraph, **kwargs: Any) -> str:
        lines = ["graph TD"]
        lines.append(f"%% OSEF {graph.metadata.name}")
        
        # Nodes
        for node in graph.nodes:
            # basic clean up for mermaid syntax
            clean_id = node.id.replace("-", "_").replace(".", "_")
            shape_open = "["
            shape_close = "]"
            
            if node.attributes.get("shape") == "folder":
                shape_open = "[/"
                shape_close = "/]"
            
            lines.append(f'    {clean_id}{shape_open}"{node.label}"{shape_close}')
            
        # Edges
        for edge in graph.edges:
            clean_source = edge.source_id.replace("-", "_").replace(".", "_")
            clean_target = edge.target_id.replace("-", "_").replace(".", "_")
            
            link = "-->"
            if edge.attributes.get("style") == "dashed":
                link = "-.->"
                
            if edge.label:
                lines.append(f'    {clean_source} {link}|{edge.label}| {clean_target}')
            else:
                lines.append(f'    {clean_source} {link} {clean_target}')

        return "\n".join(lines)

RendererRegistry.register("mermaid", MermaidRenderer)
