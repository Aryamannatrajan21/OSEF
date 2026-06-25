"""
Dependency Injection Container.
"""

from typing import Any, Callable, Dict, Type, TypeVar, cast
from osef.contracts.exceptions import ConfigurationError

T = TypeVar("T")


class Container:
    """
    Lightweight Dependency Injection Container.
    Supports singletons and lazy factories.
    """

    def __init__(self) -> None:
        self._singletons: Dict[Type[Any], Any] = {}
        self._factories: Dict[Type[Any], Callable[[], Any]] = {}

    def register_singleton(self, interface: Type[T], implementation: T) -> None:
        """Register an existing instance as a singleton."""
        self._singletons[interface] = implementation

    def register_factory(self, interface: Type[T], factory: Callable[[], T]) -> None:
        """Register a factory function for lazy resolution."""
        self._factories[interface] = factory

    def resolve(self, interface: Type[T]) -> T:
        """Resolve an interface to its implementation."""
        if interface in self._singletons:
            return cast(T, self._singletons[interface])

        if interface in self._factories:
            instance = self._factories[interface]()
            # Promote to singleton after first resolution (Lazy Singleton behavior)
            self._singletons[interface] = instance
            return cast(T, instance)

        raise ConfigurationError(f"No registered implementation for {interface}")
