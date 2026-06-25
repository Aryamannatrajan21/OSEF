"""
OSEF Core Event Models.
"""

from typing import Any, Dict
from pydantic import BaseModel, Field
import uuid


class BaseEvent(BaseModel):
    """
    Base class for all OSEF events.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str


class LifecycleEvent(BaseEvent):
    """
    Events related to the Runtime lifecycle (e.g., startup, shutdown).
    """

    state: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
