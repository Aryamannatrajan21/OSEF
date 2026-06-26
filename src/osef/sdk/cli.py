from abc import ABC, abstractmethod
from typing import Any

class CliCommand(ABC):
    """
    Allows plugins to natively inject subcommands into the `osef` CLI.
    """
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def execute(self, args: Any) -> int:
        pass
