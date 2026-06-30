"""
Repository Scanner implementation.
"""

import os
from pathlib import Path

import pathspec

from osef.scanner.models import RepositoryManifest


class RepositoryScanner:
    """
    Scans a repository directory, respecting .gitignore and producing a manifest.
    """

    DEFAULT_IGNORES = [
        ".git/",
        ".venv/",
        "venv/",
        "__pycache__/",
        ".tox/",
        ".mypy_cache/",
        ".pytest_cache/",
        "build/",
        "dist/",
    ]

    def __init__(self, root_path: str | Path):
        self.root_path = Path(root_path).resolve()
        self.spec = self._load_ignore_patterns()

    def _load_ignore_patterns(self) -> pathspec.PathSpec:  # type: ignore[type-arg]
        """Load .gitignore patterns and combine with defaults."""
        patterns = list(self.DEFAULT_IGNORES)

        gitignore_path = self.root_path / ".gitignore"
        if gitignore_path.exists():
            with open(gitignore_path, "r", encoding="utf-8") as f:
                patterns.extend(f.readlines())

        osefignore_path = self.root_path / ".osefignore"
        if osefignore_path.exists():
            with open(osefignore_path, "r", encoding="utf-8") as f:
                patterns.extend(f.readlines())

        return pathspec.PathSpec.from_lines("gitignore", patterns)

    def is_ignored(self, relative_path: str) -> bool:
        """Check if a path should be ignored."""
        return self.spec.match_file(relative_path)

    def scan(self) -> RepositoryManifest:
        """
        Scan the repository and produce a manifest.
        """
        manifest = RepositoryManifest(root_path=str(self.root_path))

        # Check metadata
        pyproject_path = self.root_path / "pyproject.toml"
        requirements_path = self.root_path / "requirements.txt"
        poetry_lock = self.root_path / "poetry.lock"
        uv_lock = self.root_path / "uv.lock"

        if pyproject_path.exists():
            manifest.has_pyproject = True
            if poetry_lock.exists():
                manifest.package_manager = "poetry"
            elif uv_lock.exists():
                manifest.package_manager = "uv"
            else:
                manifest.package_manager = "pip/hatch"

        if requirements_path.exists():
            manifest.has_requirements = True
            if not manifest.package_manager:
                manifest.package_manager = "pip"

        # Walk directory
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            dir_path = Path(dirpath)

            # Prune ignored directories
            dirnames_copy = list(dirnames)
            for d in dirnames_copy:
                rel_d = str((dir_path / d).relative_to(self.root_path)) + "/"
                if self.is_ignored(rel_d):
                    dirnames.remove(d)

            for f in filenames:
                file_path = dir_path / f
                rel_f = str(file_path.relative_to(self.root_path))

                if self.is_ignored(rel_f):
                    continue

                if f.endswith(".py"):
                    manifest.python_files.append(rel_f)
                elif (f.endswith(".ts") or f.endswith(".tsx")) and not f.endswith(
                    ".d.ts"
                ):
                    manifest.typescript_files.append(rel_f)
                elif f.endswith(".java"):
                    manifest.java_files.append(rel_f)

        return manifest
