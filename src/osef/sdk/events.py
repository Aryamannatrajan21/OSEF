from enum import Enum
from typing import Callable, Any, Dict, List


class EventType(str, Enum):
    BeforeRepositoryScan = "BeforeRepositoryScan"
    AfterRepositoryScan = "AfterRepositoryScan"
    BeforeParsing = "BeforeParsing"
    AfterParsing = "AfterParsing"
    BeforeSymbolTable = "BeforeSymbolTable"
    AfterSymbolTable = "AfterSymbolTable"
    BeforeSemanticEnrichment = "BeforeSemanticEnrichment"
    AfterSemanticEnrichment = "AfterSemanticEnrichment"
    BeforeGraphGeneration = "BeforeGraphGeneration"
    AfterGraphGeneration = "AfterGraphGeneration"
    BeforePolicyExecution = "BeforePolicyExecution"
    AfterPolicyExecution = "AfterPolicyExecution"
    BeforeAssessment = "BeforeAssessment"
    AfterAssessment = "AfterAssessment"
    BeforeReportGeneration = "BeforeReportGeneration"
    AfterReportGeneration = "AfterReportGeneration"
    BeforePluginLoad = "BeforePluginLoad"
    AfterPluginLoad = "AfterPluginLoad"


EventCallback = Callable[[EventType, Dict[str, Any]], None]


class EventBus:
    def __init__(self) -> None:
        self._subscribers: Dict[EventType, List[EventCallback]] = {
            e: [] for e in EventType
        }

    def subscribe(self, event_type: EventType, callback: EventCallback) -> None:
        self._subscribers[event_type].append(callback)

    def publish(self, event_type: EventType, payload: Dict[str, Any]) -> None:
        for callback in self._subscribers[event_type]:
            callback(event_type, payload)
