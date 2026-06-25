"""
OSEF Provider Protocols.

These protocols define the interfaces that core services must implement.
"""

from typing import Protocol, Any, Callable, Awaitable, TypeVar, runtime_checkable
from .events import BaseEvent

TEvent = TypeVar("TEvent", bound=BaseEvent)
EventHandler = Callable[[TEvent], Awaitable[None]]


@runtime_checkable
class LoggerProvider(Protocol):
    """Protocol for logging."""

    def debug(self, message: str, **kwargs: Any) -> None: ...
    def info(self, message: str, **kwargs: Any) -> None: ...
    def warning(self, message: str, **kwargs: Any) -> None: ...
    def error(self, message: str, **kwargs: Any) -> None: ...
    def critical(self, message: str, **kwargs: Any) -> None: ...


@runtime_checkable
class EventBusProvider(Protocol):
    """Protocol for the Event Bus."""

    def subscribe(
        self, event_name: str, handler: EventHandler[Any], priority: int = 0
    ) -> None: ...
    def unsubscribe(self, event_name: str, handler: EventHandler[Any]) -> None: ...
    async def publish(self, event: BaseEvent) -> None: ...


@runtime_checkable
class ConfigProvider(Protocol):
    """Protocol for Configuration management."""

    def get(self, key: str, default: Any = None) -> Any: ...
