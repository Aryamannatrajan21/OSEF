from typing import Dict, Type
from osef_visualization.projections.base import Projection
from osef_visualization.renderers.base import Renderer

class ProjectionRegistry:
    _projections: Dict[str, Type[Projection]] = {}
    
    @classmethod
    def register(cls, name: str, projection_class: Type[Projection]) -> None:
        cls._projections[name] = projection_class
        
    @classmethod
    def get(cls, name: str) -> Projection:
        if name not in cls._projections:
            raise KeyError(f"Projection '{name}' not registered.")
        return cls._projections[name]()
        
    @classmethod
    def list_projections(cls) -> list[str]:
        return list(cls._projections.keys())

class RendererRegistry:
    _renderers: Dict[str, Type[Renderer]] = {}
    
    @classmethod
    def register(cls, fmt: str, renderer_class: Type[Renderer]) -> None:
        cls._renderers[fmt] = renderer_class
        
    @classmethod
    def get(cls, fmt: str) -> Renderer:
        if fmt not in cls._renderers:
            raise KeyError(f"Renderer '{fmt}' not registered.")
        return cls._renderers[fmt]()

    @classmethod
    def list_renderers(cls) -> list[str]:
        return list(cls._renderers.keys())
