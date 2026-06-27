from typing import Any

class ArchitectureDriftProjection:
    name = "architecture_drift"
    def project(self, graph: Any, **kwargs: Any) -> Any: pass

class LayerViewProjection:
    name = "architecture_layer_view"
    def project(self, graph: Any, **kwargs: Any) -> Any: pass

class ComponentViewProjection:
    name = "architecture_component_view"
    def project(self, graph: Any, **kwargs: Any) -> Any: pass

class BoundaryViewProjection:
    name = "architecture_boundary_view"
    def project(self, graph: Any, **kwargs: Any) -> Any: pass

class DependencyViewProjection:
    name = "architecture_dependency_view"
    def project(self, graph: Any, **kwargs: Any) -> Any: pass

class ContextViewProjection:
    name = "architecture_context_view"
    def project(self, graph: Any, **kwargs: Any) -> Any: pass

class DeploymentAlignmentViewProjection:
    name = "architecture_deployment_alignment"
    def project(self, graph: Any, **kwargs: Any) -> Any: pass

class SecurityOverlayViewProjection:
    name = "architecture_security_overlay"
    def project(self, graph: Any, **kwargs: Any) -> Any: pass

def get_projections() -> dict:
    return {
        "architecture_drift": ArchitectureDriftProjection,
        "architecture_layer_view": LayerViewProjection,
        "architecture_component_view": ComponentViewProjection,
        "architecture_boundary_view": BoundaryViewProjection,
        "architecture_dependency_view": DependencyViewProjection,
        "architecture_context_view": ContextViewProjection,
        "architecture_deployment_alignment": DeploymentAlignmentViewProjection,
        "architecture_security_overlay": SecurityOverlayViewProjection
    }
