import os
from typing import List, Generator


class WorkspaceScanner:
    """Scans a workspace and yields all file paths."""

    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root

    def scan(self) -> Generator[str, None, None]:
        for root, _, files in os.walk(self.workspace_root):
            for file in files:
                yield os.path.join(root, file)


class LanguageDetector:
    """Detects and filters files belonging to a specific language."""

    def __init__(self, extensions: List[str]):
        self.extensions = extensions

    def filter(self, files: Generator[str, None, None]) -> Generator[str, None, None]:
        for file in files:
            if any(file.endswith(ext) for ext in self.extensions):
                yield file

    @classmethod
    def for_typescript(cls) -> "LanguageDetector":
        return cls(extensions=[".ts", ".tsx"])
