import os
from typing import Any
from osef.core.ekg import GraphDelta
from osef_infrastructure.adapters.base import InfrastructureAdapter
from osef_infrastructure.ikm import IKM

class DockerAdapter(InfrastructureAdapter):
    def parse(self, root_dir: str, **kwargs: Any) -> GraphDelta:
        delta = GraphDelta()
        
        dockerfile_path = os.path.join(root_dir, "Dockerfile")
        if not os.path.exists(dockerfile_path):
            return delta
            
        with open(dockerfile_path, "r") as f:
            lines = f.readlines()
            
        # Simplistic Dockerfile parsing for demonstration
        base_image = "unknown"
        ports = []
        env_vars = []
        
        for line in lines:
            line = line.strip()
            if line.startswith("FROM "):
                base_image = line.split(" ", 1)[1]
            elif line.startswith("EXPOSE "):
                ports.append(line.split(" ", 1)[1])
            elif line.startswith("ENV "):
                env_vars.append(line.split(" ", 1)[1])
                
        image_id = f"docker:image:{os.path.basename(root_dir)}"
        image_node = IKM.create_node(
            node_type=IKM.IMAGE,
            node_id=image_id,
            name="Dockerfile Image",
            source_adapter="DockerAdapter",
            source_file=dockerfile_path,
            base_image=base_image,
            ports=",".join(ports),
            env_vars=",".join(env_vars)
        )
        delta.nodes_to_add.append(image_node)
        
        return delta
