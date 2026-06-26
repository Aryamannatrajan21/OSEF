from abc import ABC, abstractmethod
from osef.sdk.pipeline import PipelineContext
from osef.parser.symbol_table import SymbolTable


class BaseProvider(ABC):
    """
    Base contract for all OSEF capabilities.
    Providers must be stateless.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        pass


class BaseParserProvider(BaseProvider):
    """
    Contract for Language Parsers.
    """

    @property
    @abstractmethod
    def language(self) -> str:
        pass

    @abstractmethod
    def parse(self, context: PipelineContext) -> SymbolTable:
        """
        Executes parsing synchronously and returns a SymbolTable.
        Must not mutate shared execution state directly.
        """
        pass
