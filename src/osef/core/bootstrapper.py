"""
Bootstrapper for OSEF Runtime Lifecycle.
"""

import logging
from osef.contracts.providers import LoggerProvider, EventBusProvider, ConfigProvider
from osef.contracts.events import LifecycleEvent
from osef.core.container import Container
from osef.core.config import DefaultConfigProvider
from osef.services.logger import DefaultLogger
from osef.services.event_bus import DefaultEventBus


class Runtime:
    """
    OSEF Runtime context.
    """

    def __init__(self) -> None:
        self.container = Container()
        self.is_running = False

    async def start(self) -> None:
        """Starts the OSEF runtime."""
        # 1. Load Config
        config = DefaultConfigProvider()
        self.container.register_singleton(ConfigProvider, config)

        # 2. Setup Logging
        level_name = config.get("log_level", "INFO").upper()
        level = getattr(logging, level_name, logging.INFO)
        logger = DefaultLogger(level=level)
        self.container.register_singleton(LoggerProvider, logger)

        logger.info("Starting OSEF Runtime...")

        # 3. Setup Event Bus
        event_bus = DefaultEventBus(logger=logger)
        self.container.register_singleton(EventBusProvider, event_bus)

        # 4. Dispatch Startup Event
        startup_event = LifecycleEvent(name="runtime.startup", state="starting")
        await event_bus.publish(startup_event)

        self.is_running = True
        logger.info("OSEF Runtime successfully started.")

    async def shutdown(self) -> None:
        """Shuts down the OSEF runtime."""
        if not self.is_running:
            return

        logger = self.container.resolve(LoggerProvider)
        logger.info("Shutting down OSEF Runtime...")

        event_bus = self.container.resolve(EventBusProvider)
        shutdown_event = LifecycleEvent(name="runtime.shutdown", state="shutting_down")
        await event_bus.publish(shutdown_event)

        self.is_running = False
        logger.info("OSEF Runtime shutdown complete.")


def bootstrap() -> Runtime:
    """
    Synchronous bootstrap entry point.
    Returns the initialized but unstarted runtime.
    """
    return Runtime()
