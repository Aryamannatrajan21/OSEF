import yaml  # type: ignore
from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class BenchmarkManifest:
    name: str
    repository: str
    tier: str
    languages: List[str]
    profiles: List[str]
    plugins: List[str]
    expected: Dict[str, Any]
    certification: Dict[str, bool]

    @classmethod
    def from_yaml(cls, path: str) -> "BenchmarkManifest":
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)
