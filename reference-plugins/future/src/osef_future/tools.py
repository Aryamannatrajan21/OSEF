from typing import Dict, Any, Callable
from pydantic import BaseModel, Field
from osef.core.reasoner import EngineeringReasoner

class GraphToolSchema(BaseModel):
    """
    Schema representing a tool that can be exposed to an LLM.
    """
    name: str
    description: str
    parameters: Dict[str, Any]

class OSEFTool:
    """
    Wraps an EngineeringReasoner method into an LLM-callable tool.
    """
    def __init__(self, name: str, description: str, func: Callable, schema: GraphToolSchema):
        self.name = name
        self.description = description
        self.func = func
        self.schema = schema
        
    def execute(self, **kwargs) -> Any:
        return self.func(**kwargs)

def build_reasoner_tools(reasoner: EngineeringReasoner) -> Dict[str, OSEFTool]:
    """
    Exposes deterministic EKG reasoning capabilities to LLMs.
    """
    tools = {}
    
    tools["dependency_chain"] = OSEFTool(
        name="dependency_chain",
        description="Traces all transitive dependencies for a given node ID.",
        func=reasoner.dependency_chain,
        schema=GraphToolSchema(
            name="dependency_chain",
            description="Traces all transitive dependencies for a given node ID.",
            parameters={
                "type": "object",
                "properties": {
                    "node_id": {"type": "string", "description": "The unique ID of the node to trace."}
                },
                "required": ["node_id"]
            }
        )
    )
    
    tools["deployment_chain"] = OSEFTool(
        name="deployment_chain",
        description="Traces a software component down to its physical/logical deployment.",
        func=reasoner.deployment_chain,
        schema=GraphToolSchema(
            name="deployment_chain",
            description="Traces a software component down to its physical/logical deployment.",
            parameters={
                "type": "object",
                "properties": {
                    "node_id": {"type": "string", "description": "The unique ID of the software component node."}
                },
                "required": ["node_id"]
            }
        )
    )
    
    return tools
