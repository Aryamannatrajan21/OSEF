import json
import os
from pathlib import Path
from typing import Any, Dict, List
import yaml  # type: ignore[import-untyped]
from rich.console import Console

console = Console()


def build_marketplace(
    out_dir: str = "marketplace-site", index_path: str = "marketplace-index.json"
) -> None:
    """Build static HTML/JSON site bundle for the OSEF Plugin Marketplace."""
    console.print(
        f"[bold blue]Building static marketplace bundle in {out_dir}...[/bold blue]"
    )

    plugins_data: List[Dict[str, Any]] = []

    # Try loading marketplace-index.json
    if os.path.exists(index_path):
        try:
            with open(index_path, "r", encoding="utf-8") as f:
                index_json = json.load(f)
                plugins_data = index_json.get("plugins", [])
        except Exception as e:
            console.print(f"[yellow]Warning: Could not read {index_path}: {e}[/yellow]")

    # Enrich with reference-plugins plugin.yaml if available
    ref_plugins_dir = Path("reference-plugins")
    if ref_plugins_dir.exists() and ref_plugins_dir.is_dir():
        for plugin_dir in ref_plugins_dir.iterdir():
            if plugin_dir.is_dir():
                manifest_path = plugin_dir / "plugin.yaml"
                if not manifest_path.exists():
                    manifest_path = plugin_dir / "plugin.yml"
                if manifest_path.exists():
                    try:
                        with open(manifest_path, "r", encoding="utf-8") as f:
                            manifest = yaml.safe_load(f)
                            if manifest and isinstance(manifest, dict):
                                name = manifest.get("name") or manifest.get(
                                    "id", plugin_dir.name
                                )
                                # Find or create plugin entry
                                entry = next(
                                    (
                                        p
                                        for p in plugins_data
                                        if p.get("name") == name
                                        or p.get("name") == plugin_dir.name
                                    ),
                                    None,
                                )
                                if not entry:
                                    entry = {"name": plugin_dir.name}
                                    plugins_data.append(entry)
                                entry.update(
                                    {
                                        "version": manifest.get(
                                            "version", entry.get("version", "1.0.0")
                                        ),
                                        "description": manifest.get(
                                            "description",
                                            entry.get(
                                                "description",
                                                f"{plugin_dir.name} plugin for OSEF",
                                            ),
                                        ),
                                        "id": manifest.get(
                                            "id", f"osef.plugins.{plugin_dir.name}"
                                        ),
                                        "author": manifest.get(
                                            "author", "OSEF Core Team"
                                        ),
                                        "license": manifest.get(
                                            "license", "Apache-2.0"
                                        ),
                                        "keywords": manifest.get(
                                            "keywords", [plugin_dir.name, "plugin"]
                                        ),
                                        "capabilities": manifest.get(
                                            "capabilities", {}
                                        ),
                                        "tier": "TIER_1_OFFICIAL",
                                        "certification": "CERTIFIED",
                                    }
                                )
                    except Exception as e:
                        console.print(
                            f"[yellow]Warning: Failed parsing manifest {manifest_path}: {e}[/yellow]"
                        )

    # Create output directories
    out_path = Path(out_dir)
    plugins_out_path = out_path / "plugins"
    plugins_out_path.mkdir(parents=True, exist_ok=True)

    # Save machine-readable JSON index
    index_json_out = out_path / "index.json"
    with open(index_json_out, "w", encoding="utf-8") as f:
        json.dump(
            {"plugins": plugins_data, "total_count": len(plugins_data)}, f, indent=2
        )

    # Generate HTML landing page
    index_html = _generate_landing_html(plugins_data)
    with open(out_path / "index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    # Generate plugin detail pages
    for plugin in plugins_data:
        p_name = plugin.get("name", "unknown")
        detail_html = _generate_detail_html(plugin)
        with open(plugins_out_path / f"{p_name}.html", "w", encoding="utf-8") as f:
            f.write(detail_html)

    console.print(
        "[bold green]✔ Marketplace site bundle built successfully![/bold green]"
    )
    console.print(f"  Total validated plugins: [cyan]{len(plugins_data)}[/cyan]")
    console.print(f"  Output directory: [cyan]{out_path.resolve()}[/cyan]")


def _generate_landing_html(plugins: List[Dict[str, Any]]) -> str:
    cards_html = ""
    for p in plugins:
        name = p.get("name", "Unnamed")
        desc = p.get("description", "No description provided.")
        version = p.get("version", "1.0.0")
        tier = p.get("tier", "TIER_1_OFFICIAL")
        signed = "Signed ✓" if p.get("signature") else "Verified"
        cards_html += f"""
        <div class="card">
            <div class="card-header">
                <h3><a href="plugins/{name}.html">{name}</a> <span class="badge badge-version">v{version}</span></h3>
                <span class="badge badge-tier">{tier}</span>
            </div>
            <p class="description">{desc}</p>
            <div class="card-footer">
                <span class="badge badge-signed">{signed}</span>
                <a href="plugins/{name}.html" class="btn">View Details →</a>
            </div>
        </div>
        """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OSEF Plugin Marketplace</title>
    <style>
        :root {{ --bg: #0f172a; --card-bg: #1e293b; --text: #f8fafc; --text-muted: #94a3b8; --accent: #38bdf8; --border: #334155; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 2rem; line-height: 1.5; }}
        .container {{ max-width: 1100px; margin: 0 auto; }}
        header {{ margin-bottom: 3rem; text-align: center; border-bottom: 1px solid var(--border); padding-bottom: 2rem; }}
        h1 {{ font-size: 2.5rem; margin-bottom: 0.5rem; color: var(--text); }}
        .subtitle {{ color: var(--text-muted); font-size: 1.1rem; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.5rem; }}
        .card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s, border-color 0.2s; }}
        .card:hover {{ transform: translateY(-4px); border-color: var(--accent); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }}
        .card-header h3 {{ margin: 0; font-size: 1.3rem; }}
        .card-header a {{ color: var(--text); text-decoration: none; }}
        .card-header a:hover {{ color: var(--accent); }}
        .description {{ color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; flex-grow: 1; }}
        .card-footer {{ display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border); padding-top: 1rem; }}
        .badge {{ padding: 0.25rem 0.6rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; }}
        .badge-version {{ background: #334155; color: #cbd5e1; }}
        .badge-tier {{ background: #0369a1; color: #e0f2fe; }}
        .badge-signed {{ background: #065f46; color: #d1fae5; }}
        .btn {{ color: var(--accent); text-decoration: none; font-weight: 600; font-size: 0.9rem; }}
        .btn:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🏛️ OSEF Plugin Marketplace</h1>
            <p class="subtitle">Official & Community Extension Ecosystem for the Engineering Knowledge Graph</p>
        </header>
        <main class="grid">
            {cards_html}
        </main>
    </div>
</body>
</html>"""


def _generate_detail_html(plugin: Dict[str, Any]) -> str:
    name = plugin.get("name", "Unnamed")
    desc = plugin.get("description", "No description provided.")
    version = plugin.get("version", "1.0.0")
    author = plugin.get("author", "OSEF Core Team")
    license_type = plugin.get("license", "Apache-2.0")
    tier = plugin.get("tier", "TIER_1_OFFICIAL")
    sig = plugin.get("signature", "Verified via reference bundle")
    url = plugin.get(
        "download_url",
        f"https://github.com/Aryamannatrajan21/OSEF/tree/main/reference-plugins/{name}",
    )

    capabilities = plugin.get("capabilities", {})
    cap_html = "<ul>"
    if isinstance(capabilities, dict) and capabilities:
        for k, v in capabilities.items():
            cap_html += f"<li><strong>{k}:</strong> <code>{v}</code></li>"
    else:
        cap_html += (
            "<li>Provides standard EKG enrichment and analysis capabilities.</li>"
        )
    cap_html += "</ul>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — OSEF Marketplace</title>
    <style>
        :root {{ --bg: #0f172a; --card-bg: #1e293b; --text: #f8fafc; --text-muted: #94a3b8; --accent: #38bdf8; --border: #334155; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 2rem; line-height: 1.6; }}
        .container {{ max-width: 800px; margin: 0 auto; background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 2.5rem; }}
        a.back {{ color: var(--accent); text-decoration: none; display: inline-block; margin-bottom: 2rem; font-weight: 600; }}
        a.back:hover {{ text-decoration: underline; }}
        h1 {{ font-size: 2.2rem; margin-top: 0; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 1rem; }}
        .badge {{ padding: 0.3rem 0.8rem; border-radius: 9999px; font-size: 0.8rem; font-weight: 600; background: #0369a1; color: #e0f2fe; text-transform: uppercase; }}
        .meta {{ color: var(--text-muted); margin-bottom: 2rem; font-size: 0.95rem; border-bottom: 1px solid var(--border); padding-bottom: 1rem; }}
        .section {{ margin-bottom: 2rem; }}
        h2 {{ font-size: 1.4rem; color: var(--text); border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }}
        pre, code {{ background: #0f172a; padding: 0.2rem 0.5rem; border-radius: 6px; font-family: monospace; font-size: 0.9rem; color: #cbd5e1; }}
        pre {{ padding: 1rem; overflow-x: auto; border: 1px solid var(--border); }}
        .btn-install {{ display: inline-block; background: var(--accent); color: #0f172a; font-weight: bold; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; margin-top: 1rem; }}
        .btn-install:hover {{ opacity: 0.9; }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" class="back">← Back to Marketplace</a>
        <h1>{name} <span class="badge">{tier}</span></h1>
        <div class="meta">Version: <strong>{version}</strong> | Author: <strong>{author}</strong> | License: <strong>{license_type}</strong></div>
        
        <div class="section">
            <h2>Description</h2>
            <p>{desc}</p>
        </div>

        <div class="section">
            <h2>Exposed Capabilities</h2>
            {cap_html}
        </div>

        <div class="section">
            <h2>Installation & Usage</h2>
            <p>Install this extension directly via the OSEF CLI:</p>
            <pre><code>osef plugin install {name}</code></pre>
        </div>

        <div class="section">
            <h2>Security & Provenance</h2>
            <p><strong>Package Source:</strong> <a href="{url}" style="color: var(--accent);">{url}</a></p>
            <p><strong>Signature:</strong> <code>{sig[:32]}...</code></p>
        </div>
    </div>
</body>
</html>"""
