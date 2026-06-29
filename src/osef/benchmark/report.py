import os
import json
from .manifest import BenchmarkManifest
from typing import Dict, Any

class BenchmarkReport:
    def __init__(self, manifest: BenchmarkManifest, metrics: Dict[str, Any], certification: Dict[str, Any]):
        self.manifest = manifest
        self.metrics = metrics
        self.certification = certification
        self.output_dir = f"benchmarks/results/latest/{manifest.name}"
        os.makedirs(self.output_dir, exist_ok=True)

    def get_summary(self) -> Dict[str, Any]:
        return {
            "name": self.manifest.name,
            "success": self.certification.get("success", False)
        }

    def generate_all(self) -> None:
        self._write_json("report.json", self.get_summary())
        self._write_json("metrics.json", self.metrics)
        self._write_json("validation.json", self.certification)
        self._write_json("dashboard.json", {**self.get_summary(), **self.metrics})
        self._write_md("report.md", f"# Benchmark Report: {self.manifest.name}\n\nSuccess: {self.certification.get('success', False)}")

    def _write_json(self, filename: str, data: Dict[str, Any]) -> None:
        with open(os.path.join(self.output_dir, filename), "w") as f:
            json.dump(data, f, indent=2)

    def _write_md(self, filename: str, content: str) -> None:
        with open(os.path.join(self.output_dir, filename), "w") as f:
            f.write(content)
