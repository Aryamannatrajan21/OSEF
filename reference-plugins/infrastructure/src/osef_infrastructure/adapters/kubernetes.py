import os
import yaml
from typing import Any
from osef.core.ekg import GraphDelta
from osef_infrastructure.adapters.base import InfrastructureAdapter
from osef_infrastructure.ikm import IKM

class KubernetesAdapter(InfrastructureAdapter):
    def parse(self, root_dir: str, **kwargs: Any) -> GraphDelta:
        delta = GraphDelta()
        
        # In a real plugin, this would walk the directory finding .yaml files.
        # For validation, we'll just check a typical k8s/ deployment folder if it exists.
        k8s_dir = os.path.join(root_dir, "k8s")
        if not os.path.exists(k8s_dir):
            return delta
            
        for file in os.listdir(k8s_dir):
            if not file.endswith((".yaml", ".yml")):
                continue
                
            path = os.path.join(k8s_dir, file)
            with open(path, "r") as f:
                try:
                    # Some k8s files have multiple documents
                    docs = yaml.safe_load_all(f)
                    for doc in docs:
                        if not doc or not isinstance(doc, dict):
                            continue
                            
                        kind = doc.get("kind")
                        metadata = doc.get("metadata", {})
                        name = metadata.get("name", "unknown")
                        
                        if kind == "Deployment":
                            dep_id = f"k8s:deployment:{name}"
                            dep_node = IKM.create_node(
                                node_type=IKM.DEPLOYMENT, 
                                node_id=dep_id, 
                                name=name,
                                source_adapter="KubernetesAdapter",
                                source_file=path
                            )
                            delta.nodes_to_add.append(dep_node)
                            
                            # Inspect containers
                            containers = doc.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
                            for container in containers:
                                c_name = container.get("name")
                                c_image = container.get("image")
                                c_id = f"k8s:container:{name}:{c_name}"
                                c_node = IKM.create_node(
                                    node_type=IKM.CONTAINER, 
                                    node_id=c_id, 
                                    name=c_name, 
                                    source_adapter="KubernetesAdapter",
                                    source_file=path,
                                    image=c_image
                                )
                                delta.nodes_to_add.append(c_node)
                                
                                edge = IKM.create_edge(dep_id, c_id, IKM.DEPLOYED_TO)
                                delta.edges_to_add.append(edge)
                                
                        elif kind == "Service":
                            svc_id = f"k8s:service:{name}"
                            svc_node = IKM.create_node(
                                node_type=IKM.SERVICE, 
                                node_id=svc_id, 
                                name=name,
                                source_adapter="KubernetesAdapter",
                                source_file=path
                            )
                            delta.nodes_to_add.append(svc_node)
                            
                except yaml.YAMLError:
                    delta.diagnostics.append({"error": f"Failed to parse k8s yaml: {file}"})
                    
        return delta
