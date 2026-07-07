from pathlib import Path
from typer.testing import CliRunner
from osef.cli.main import app

runner = CliRunner()


def test_marketplace_build(tmp_path: Path):
    out_dir = tmp_path / "test_market_site"
    result = runner.invoke(app, ["plugin", "build", "--out-dir", str(out_dir)])
    assert result.exit_code == 0
    assert out_dir.exists()
    assert (out_dir / "index.html").exists()
    assert (out_dir / "index.json").exists()
    assert (out_dir / "plugins").exists()
