"""
Default Logger Implementation.
"""

import logging
import sys
from typing import Any
from osef.contracts.providers import LoggerProvider


class DefaultLogger(LoggerProvider):
    """
    Standard library based structured logger.
    """

    def __init__(self, name: str = "osef", level: int = logging.INFO) -> None:
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

        if not self._logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self._logger.addHandler(handler)

    def _format_msg(self, message: str, **kwargs: Any) -> str:
        if kwargs:
            context = " | " + " ".join(f"{k}={v}" for k, v in kwargs.items())
            return f"{message}{context}"
        return message

    def debug(self, message: str, **kwargs: Any) -> None:
        self._logger.debug(self._format_msg(message, **kwargs))

    def info(self, message: str, **kwargs: Any) -> None:
        self._logger.info(self._format_msg(message, **kwargs))

    def warning(self, message: str, **kwargs: Any) -> None:
        self._logger.warning(self._format_msg(message, **kwargs))

    def error(self, message: str, **kwargs: Any) -> None:
        self._logger.error(self._format_msg(message, **kwargs))

    def critical(self, message: str, **kwargs: Any) -> None:
        self._logger.critical(self._format_msg(message, **kwargs))
