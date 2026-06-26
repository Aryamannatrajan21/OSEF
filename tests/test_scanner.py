from osef.scanner.scanner import RepositoryScanner


def test_scanner_discovers_python_files(tmp_path):
    # Setup mock repo
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("print('hello')")
    (tmp_path / "pyproject.toml").write_text("[project]")
    (tmp_path / "requirements.txt").write_text("typer")

    # Add ignored dir
    (tmp_path / ".venv").mkdir()
    (tmp_path / ".venv" / "ignore_me.py").write_text("")

    # Custom ignore
    (tmp_path / ".gitignore").write_text("ignore_this.py\n")
    (tmp_path / "ignore_this.py").write_text("")

    scanner = RepositoryScanner(tmp_path)
    manifest = scanner.scan()

    assert manifest.has_pyproject is True
    assert manifest.has_requirements is True
    assert len(manifest.python_files) == 1
    # Depending on OS, path separator might differ in strings, but pathlib standardizes
    # Let's check if the basename is in there
    assert "src/main.py" in manifest.python_files[0]
