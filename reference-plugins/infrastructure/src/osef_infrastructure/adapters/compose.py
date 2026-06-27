import os
import yaml
from typing import Any
from osef.core.ekg import GraphDelta
from osef_infrastructure.adapters.base import InfrastructureAdapter
from osef_infrastructure.ikm import IKM

class ComposeAdapter(InfrastructureAdapter):
    def parse(self, root_dir: str, **kwargs: Any) -> GraphDelta:
        delta = GraphDelta()
        
        compose_path = os.path.join(root_dir, "docker-compose.yml")
        if not os.path.exists(compose_path):
            return delta
            
        with open(compose_path, "r") as f:
            try:
                data = yaml.safe_load(f)
            except yaml.YAMLError:
                delta.diagnostics.append({"error": "Failed to parse docker-compose.yml"})
                return delta
                
        if not data or not isinstance(data, dict):
            return delta
            
        services = data.get("services", {})
        for svc_name, svc_data in services.items():
            svc_id = f"compose:service:{svc_name}"
            svc_node = IKM.create_node(
                node_type=IKM.SERVICE,
                node_id=svc_id,
                name=svc_name,
                source_adapter="ComposeAdapter",
                source_file=compose_path,
                image=svc_data.get("image", "build")
            )
            delta.nodes_to_add.append(svc_node)
            
            # Map depends_on
            if "depends_on" in svc_data:
                deps = svc_data["depends_on"]
                if isinstance(deps, list):
                    for dep in deps:
                        dep_id = f"compose:service:{dep}"
                        edge = IKM.create_edge(
                            source_id=svc_id,
                            target_id=dep_id,
                            relation_type=IKM.REQUIRES
                        )
                        delta.edges_to_add.append(edge)
                        
            # Map volumes
            volumes = svc_data.get("volumes", [])
            for vol in volumes:
                if isinstance(vol, str):
                    vol_name = vol.split(":")[0]
                    vol_id = f"compose:volume:{vol_name}"
                    # Just add the volume node if it doesn't exist (simplistic)
                    vol_node = IKM.create_node(
                        node_type=IKM.VOLUME, 
                        node_id=vol_id, 
                        name=vol_name,
                        source_adapter="ComposeAdapter",
                        source_file=compose_path
                    )
                    delta.nodes_to_add.append(vol_node)
                    edge = IKM.create_edge(svc_id, vol_id, IKM.MOUNTS)
                    delta.edges_to_add.append(edge)
                    
        return delta
