from typing import List, Dict, Any, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class ProjectionMetadata(BaseModel):
    name: str
    version: str
    graph_schema: str = "osef.graph/1.0"
    generated_by: str = "osef-visualization"
    execution_id: Optional[str] = None
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    filters: Dict[str, Any] = Field(default_factory=dict)
    renderer_hints: Dict[str, Any] = Field(default_factory=dict)
    statistics: Dict[str, Any] = Field(default_factory=dict)

class ProjectedNode(BaseModel):
    id: str
    type: str
    label: str
    attributes: Dict[str, Any] = Field(default_factory=dict)
    
class ProjectedEdge(BaseModel):
    source_id: str
    target_id: str
    type: str
    label: Optional[str] = None
    attributes: Dict[str, Any] = Field(default_factory=dict)

class ProjectedGraph(BaseModel):
    """
    Intermediate Representation (IR) for the Engineering Knowledge Graph.
    Decouples the EKG from the Renderers.
    """
    metadata: ProjectionMetadata
    nodes: List[ProjectedNode] = Field(default_factory=list)
    edges: List[ProjectedEdge] = Field(default_factory=list)
