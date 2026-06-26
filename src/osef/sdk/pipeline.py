import logging
from dataclasses import dataclass, field
from typing import Any, Dict
from pathlib import Path

from osef.scanner.models import RepositoryManifest
from osef.sdk.context import ExtensionContext

# We can define more structured metrics/cancellation logic later.
# For now, simple stubs are sufficient to establish the contract.

class MetricsCollector:
    def record(self, metric_name: str, value: Any) -> None:
        pass

class CancellationToken:
    def __init__(self):
        self.is_cancelled = False
        
    def cancel(self):
        self.is_cancelled = True

class ProgressReporter:
    def report(self, percentage: float, status: str) -> None:
        pass


@dataclass
class PipelineContext:
    """
    The immutable execution contract for OSEF capabilities.
    Providers receive ONLY this object during execution.
    """
    manifest: RepositoryManifest
    workspace_dir: Path
    extension_context: ExtensionContext
    
    # Execution State utilities
    logger: logging.Logger = field(default_factory=lambda: logging.getLogger("osef.pipeline"))
    metrics: MetricsCollector = field(default_factory=MetricsCollector)
    cancellation_token: CancellationToken = field(default_factory=CancellationToken)
    progress: ProgressReporter = field(default_factory=ProgressReporter)
    
    # Project config could be injected here if we add a formal Config model.
    config: Dict[str, Any] = field(default_factory=dict)
