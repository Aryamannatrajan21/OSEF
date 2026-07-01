from typing import Any


class SecurityBlastRadiusProjection:
    name = "security_blast_radius"
    description = (
        "Projects vulnerability spread across connected infrastructure and software"
    )

    def project(self, graph: Any, **kwargs: Any) -> Any:
        # Returns generic ProjectedGraph IR
        pass


class AttackSurfaceProjection:
    name = "attack_surface"
    description = "Projects all external ingress points mapped to internal assets"

    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass


def get_projections() -> dict:
    return {
        "security_blast_radius": SecurityBlastRadiusProjection,
        "attack_surface": AttackSurfaceProjection,
    }
