import os
import shutil
from .report import BenchmarkReport

class BenchmarkHistory:
    def __init__(self, history_dir: str = "benchmarks/history", current_version: str = "v1.0.0"):
        self.history_dir = history_dir
        self.current_version = current_version

    def archive(self, benchmark_name: str, report: BenchmarkReport) -> None:
        target_dir = os.path.join(self.history_dir, self.current_version, benchmark_name)
        os.makedirs(target_dir, exist_ok=True)
        
        # Copy from latest to history
        src_dir = f"benchmarks/results/latest/{benchmark_name}"
        if os.path.exists(src_dir):
            for file in os.listdir(src_dir):
                shutil.copy2(os.path.join(src_dir, file), os.path.join(target_dir, file))
