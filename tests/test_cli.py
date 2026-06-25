from typer.testing import CliRunner
from osef.cli.main import app

runner = CliRunner()


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Open Source Engineering Framework" in result.stdout


def test_cli_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "osef version" in result.stdout


def test_cli_doctor():
    result = runner.invoke(app, ["doctor"])
    assert result.exit_code == 0
    assert "Diagnostics complete" in result.stdout


def test_cli_init(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    assert "Project initialized successfully" in result.stdout
    assert (tmp_path / "osef.toml").exists()

    # Test second init prints warning
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    assert "already exists" in result.stdout


def test_cli_validate():
    result = runner.invoke(app, ["validate"])
    assert result.exit_code == 0
    assert "Validation passed" in result.stdout


def test_cli_config():
    result = runner.invoke(app, ["config"])
    assert result.exit_code == 0
    assert "Active Configuration" in result.stdout


def test_cli_info():
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "OSEF Version" in result.stdout


def test_cli_graph():
    result = runner.invoke(app, ["graph"])
    assert result.exit_code == 0
    assert "Engineering Knowledge Graph operations" in result.stdout


def test_cli_docs(monkeypatch):
    # Mock subprocess.run to avoid actually starting mkdocs
    import subprocess

    def mock_run(*args, **kwargs):
        return subprocess.CompletedProcess(args=args[0], returncode=0)

    monkeypatch.setattr(subprocess, "run", mock_run)

    result = runner.invoke(app, ["docs"])
    assert result.exit_code == 0
    assert "Starting MkDocs documentation server" in result.stdout


def test_cli_docs_failure(monkeypatch):
    import subprocess

    def mock_run_fail(*args, **kwargs):
        raise subprocess.CalledProcessError(1, cmd="mkdocs")

    monkeypatch.setattr(subprocess, "run", mock_run_fail)

    result = runner.invoke(app, ["docs"])
    assert result.exit_code == 1
    assert "Failed to start MkDocs server" in result.stdout
