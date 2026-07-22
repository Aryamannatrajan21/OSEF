"""
Import Resolution Engine.
"""

from osef.parser.symbol_table import SymbolTable


class ImportResolver:
    """
    Resolves import statements to concrete symbols within the SymbolTable.
    """

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    def _get_project_dependencies(self) -> set[str]:
        if getattr(self, "_project_deps", None) is not None:
            return self._project_deps
        deps = {
            "fastapi",
            "uvicorn",
            "litellm",
            "boto3",
            "pytest",
            "librosa",
            "numpy",
            "typer",
            "pydantic",
            "jinja2",
            "rich",
            "pathspec",
            "yaml",
            "cryptography",
            "httpx",
            "next",
            "react",
            "lucide-react",
            "react-markdown",
            "remark-gfm",
            "react-force-graph-2d",
            "react-force-graph-3d",
        }
        from pathlib import Path
        import json
        import re

        for p in [Path.cwd(), *Path.cwd().parents]:
            if (p / "pyproject.toml").exists():
                for py_file in p.rglob("pyproject.toml"):
                    if "node_modules" in str(py_file) or ".venv" in str(py_file):
                        continue
                    try:
                        content = py_file.read_text(errors="ignore")
                        for line in content.splitlines():
                            m = re.findall(r'"([a-zA-Z0-9_\-]+)(?:[><=~\[].*)?"', line)
                            for dep in m:
                                deps.add(dep.lower())
                                deps.add(dep.split("-")[0].lower())
                    except Exception:
                        pass
                for req_file in p.rglob("requirements*.txt"):
                    if "node_modules" in str(req_file) or ".venv" in str(req_file):
                        continue
                    try:
                        for line in req_file.read_text(errors="ignore").splitlines():
                            line = line.strip().split("#")[0]
                            if line and not line.startswith("-"):
                                dep = re.split(r"[><=~\[!]", line)[0].strip().lower()
                                if dep:
                                    deps.add(dep)
                                    deps.add(dep.split("-")[0].lower())
                    except Exception:
                        pass
                for pkg_file in p.rglob("package.json"):
                    if "node_modules" in str(pkg_file):
                        continue
                    try:
                        data = json.loads(pkg_file.read_text(errors="ignore"))
                        for sec in (
                            "dependencies",
                            "devDependencies",
                            "peerDependencies",
                        ):
                            if sec in data and isinstance(data[sec], dict):
                                for k in data[sec].keys():
                                    deps.add(k.split("/")[0])
                                    deps.add(k)
                    except Exception:
                        pass
                break
        self._project_deps = deps
        return self._project_deps

    def resolve(self) -> None:
        """
        Attempt to resolve all imports.
        """
        imports = self.symbol_table.find_by_type("import")
        modules = self.symbol_table.find_by_type("module")

        for imp in imports:
            # Mark as unresolved by default
            imp.metadata["resolved"] = "false"

            # Simple heuristic matching for now
            target = imp.metadata.get("module") or imp.name

            # Search for matching module
            target_path = target.replace(".", "/")
            for mod in modules:
                # If the module's file path loosely matches the import target
                if target_path in mod.file_path:
                    imp.metadata["resolved"] = "true"
                    imp.metadata["resolved_to"] = mod.id
                    break

            if imp.metadata.get("resolved") != "true":
                if target.startswith(("@/", "./", "../")) or target.split("/")[0] in (
                    "@",
                    ".",
                ):
                    imp.metadata["resolved"] = "true"
                    imp.metadata["resolved_to"] = f"alias:{target}"
                    imp.metadata["is_external"] = "false"
                    continue

                top_level = target.split(".")[0].split("/")[0]
                try:
                    import sys
                    import importlib.util

                    deps = self._get_project_dependencies()
                    if top_level in getattr(sys, "stdlib_module_names", ()):
                        imp.metadata["resolved"] = "true"
                        imp.metadata["resolved_to"] = f"stdlib:{top_level}"
                        imp.metadata["is_external"] = "true"
                    elif (
                        top_level.lower() in deps
                        or target.split("/")[0] in deps
                        or importlib.util.find_spec(top_level) is not None
                    ):
                        imp.metadata["resolved"] = "true"
                        imp.metadata["resolved_to"] = f"package:{top_level}"
                        imp.metadata["is_external"] = "true"
                except Exception:
                    pass
