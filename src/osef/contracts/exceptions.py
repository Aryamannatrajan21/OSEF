"""
OSEF Exception Hierarchy.
"""


class OSEFError(Exception):
    """Base exception for all OSEF errors."""

    pass


class ConfigurationError(OSEFError):
    """Raised when configuration is invalid or missing."""

    pass


class RuntimeError(OSEFError):
    """Raised when a runtime error occurs."""

    pass


class PluginError(OSEFError):
    """Raised when a plugin fails to load or execute."""

    pass


class KnowledgeError(OSEFError):
    """Raised during EKK parsing or operations."""

    pass


class ValidationError(OSEFError):
    """Raised when validation of an entity or event fails."""

    pass


class EventError(OSEFError):
    """Raised when event dispatching fails."""

    pass


class ArchitectureViolation(OSEFError):
    """Raised when an architectural constraint is violated."""

    pass
