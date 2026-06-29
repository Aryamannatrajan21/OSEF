import os
from typing import List, Optional
from .manifest import BenchmarkManifest


class BenchmarkRegistry:
    def __init__(self, base_dir: str = "benchmarks/official"):
        self.base_dir = base_dir
        self.manifests: List[BenchmarkManifest] = []

    def load_all(self) -> None:
        for tier in ["tier1", "tier2", "tier3", "tier4"]:
            tier_dir = os.path.join(self.base_dir, tier)
            if not os.path.exists(tier_dir):
                continue
            for file in os.listdir(tier_dir):
                if file.endswith(".yaml"):
                    self.manifests.append(
                        BenchmarkManifest.from_yaml(os.path.join(tier_dir, file))
                    )

    def get_by_name(self, name: str) -> Optional[BenchmarkManifest]:
        for manifest in self.manifests:
            if manifest.name == name:
                return manifest
        return None

    def get_by_tier(self, tier: str) -> List[BenchmarkManifest]:
        return [m for m in self.manifests if m.tier == tier]
