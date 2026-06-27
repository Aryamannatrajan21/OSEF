from enum import Enum
from typing import Dict, Any

class RuntimeNodeType(str, Enum):
    PROCESS = "Runtime.Process"
    THREAD = "Runtime.Thread"
    EXECUTION = "Runtime.Execution"
    REQUEST = "Runtime.Request"
    TRANSACTION = "Runtime.Transaction"
    EVENT = "Runtime.Event"
    QUEUE = "Runtime.Queue"
    MESSAGE = "Runtime.Message"
    TRACE = "Runtime.Trace"
    SPAN = "Runtime.Span"
    SESSION = "Runtime.Session"
    JOB = "Runtime.Job"
    WORKER = "Runtime.Worker"
    SCHEDULE = "Runtime.Schedule"
    RESOURCE_USAGE = "Runtime.ResourceUsage"

class RuntimeKnowledgeModel:
    @staticmethod
    def get_schema() -> Dict[str, Any]:
        return {
            node.value: {"description": f"{node.value} in the Runtime Knowledge Domain"}
            for node in RuntimeNodeType
        }
