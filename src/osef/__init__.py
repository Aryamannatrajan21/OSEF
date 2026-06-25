"""
OSEF Core Package.

This package exposes the programmatic SDK interface.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("osef")
except PackageNotFoundError:
    __version__ = "unknown"
