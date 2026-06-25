"""
Async Event Bus implementation.
"""

import asyncio
from typing import Any, Dict, List, Tuple
from osef.contracts.events import BaseEvent
from osef.contracts.providers import EventHandler, EventBusProvider, LoggerProvider


class DefaultEventBus(EventBusProvider):
    """
    Default asynchronous event bus implementation.
    """

    def __init__(self, logger: LoggerProvider) -> None:
        self._logger = logger
        # Map of event name -> List of (priority, handler)
        self._subscribers: Dict[str, List[Tuple[int, EventHandler[Any]]]] = {}

    def subscribe(
        self, event_name: str, handler: EventHandler[Any], priority: int = 0
    ) -> None:
        """Subscribe to an event."""
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []

        # Add and sort by priority (higher priority first)
        self._subscribers[event_name].append((priority, handler))
        self._subscribers[event_name].sort(key=lambda x: x[0], reverse=True)
        self._logger.debug(f"Subscribed handler to {event_name} (priority {priority})")

    def unsubscribe(self, event_name: str, handler: EventHandler[Any]) -> None:
        """Unsubscribe from an event."""
        if event_name in self._subscribers:
            self._subscribers[event_name] = [
                h for h in self._subscribers[event_name] if h[1] != handler
            ]
            self._logger.debug(f"Unsubscribed handler from {event_name}")

    async def publish(self, event: BaseEvent) -> None:
        """Publish an event to all subscribers."""
        self._logger.debug(f"Publishing event: {event.name} (ID: {event.id})")

        handlers = self._subscribers.get(event.name, [])
        if not handlers:
            self._logger.debug(f"No subscribers for event: {event.name}")
            return

        tasks = []
        for priority, handler in handlers:
            tasks.append(self._execute_handler(handler, event))

        # Execute handlers concurrently
        # Note: If we need strictly sequential execution based on priority,
        # we would `await` in the loop instead of using `asyncio.gather`.
        # For now, we dispatch concurrently but log errors safely.
        await asyncio.gather(*tasks)

    async def _execute_handler(
        self, handler: EventHandler[Any], event: BaseEvent
    ) -> None:
        try:
            await handler(event)
        except Exception as e:
            self._logger.error(f"Error handling event {event.name}: {str(e)}")
            # In a robust implementation, we might record errors inside the event or trigger a failure event
