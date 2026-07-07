from pathlib import Path
from typer.testing import CliRunner
from osef.cli.main import app

runner = CliRunner()


def test_benchmark_publish(tmp_path: Path):
    out_dir = tmp_path / "test_bench_site"
    # Run against current directory
    result = runner.invoke(
        app, ["benchmark", "publish", "--target", ".", "--out-dir", str(out_dir)]
    )
    assert result.exit_code == 0
    assert out_dir.exists()
    assert (out_dir / "index.html").exists()
    assert (out_dir / "results.json").exists()
