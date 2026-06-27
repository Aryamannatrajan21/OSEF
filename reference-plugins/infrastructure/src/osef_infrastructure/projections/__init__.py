from typing import Any
from .deployment import DeploymentTopologyProjection

class NetworkTopologyProjection:
    name = "network_topology"
    description = "Shows network connections, ingresses, and services"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

class ArchitectureProjection:
    name = "infrastructure_architecture"
    description = "Shows overall infrastructure components"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

class SecurityBoundariesProjection:
    name = "security_boundaries"
    description = "Shows security groups and boundaries"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

class ContainerRelationshipsProjection:
    name = "container_relationships"
    description = "Shows container-to-container communication"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

class RuntimeDependenciesProjection:
    name = "runtime_dependencies"
    description = "Shows runtime required dependencies"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

class StorageProjection:
    name = "storage"
    description = "Shows volume and persistent storage mappings"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

class IngressProjection:
    name = "ingress"
    description = "Shows traffic ingress routing"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

class ClusterLayoutProjection:
    name = "cluster_layout"
    description = "Shows cluster nodes and namespaces"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

class CloudResourcesProjection:
    name = "cloud_resources"
    description = "Shows managed cloud resources (AWS, GCP, etc.)"
    def project(self, graph: Any, **kwargs: Any) -> Any:
        pass

def get_projections() -> dict:
    return {
        "deployment_topology": DeploymentTopologyProjection,
        "network_topology": NetworkTopologyProjection,
        "infrastructure_architecture": ArchitectureProjection,
        "security_boundaries": SecurityBoundariesProjection,
        "container_relationships": ContainerRelationshipsProjection,
        "runtime_dependencies": RuntimeDependenciesProjection,
        "storage": StorageProjection,
        "ingress": IngressProjection,
        "cluster_layout": ClusterLayoutProjection,
        "cloud_resources": CloudResourcesProjection
    }
