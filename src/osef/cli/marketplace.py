import typer
import os
from typing import Optional
from rich.console import Console
from rich.table import Table
from osef.sdk.ecosystem.security import PluginSigner
from osef.sdk.ecosystem.marketplace import MarketplaceClient

app = typer.Typer(help="Manage OSEF plugins via the Marketplace.")
console = Console()

DEFAULT_INDEX_URL = "https://raw.githubusercontent.com/Aryamannatrajan21/OSEF/main/marketplace-index.json"


@app.command("keygen")
def keygen(out_dir: str = ".") -> None:
    """Generate a new ed25519 keypair for signing plugins."""
    try:
        priv, pub = PluginSigner.generate_keypair()
        priv_path = os.path.join(out_dir, "plugin_private_key.pem")
        pub_path = os.path.join(out_dir, "plugin_public_key.pem")

        with open(priv_path, "wb") as f:
            f.write(priv)
        with open(pub_path, "wb") as f:
            f.write(pub)

        console.print("[bold green]Keypair generated successfully![/bold green]")
        console.print(f"Private Key: {priv_path}")
        console.print(f"Public Key: {pub_path}")
    except Exception as e:
        console.print(f"[bold red]Error generating keypair: {e}[/bold red]")
        raise typer.Exit(1)


@app.command("sign")
def sign(plugin_path: str, private_key_path: str) -> None:
    """Sign a plugin tar.gz package."""
    try:
        with open(private_key_path, "rb") as f:
            priv_pem = f.read()

        signature = PluginSigner.sign_file(plugin_path, priv_pem)

        console.print("[bold green]Successfully signed plugin![/bold green]")
        console.print(f"Signature (hex): {signature.hex()}")
    except Exception as e:
        console.print(f"[bold red]Error signing plugin: {e}[/bold red]")
        raise typer.Exit(1)


@app.command("search")
def search(query: str, index_url: str = DEFAULT_INDEX_URL) -> None:
    """Search for plugins in the marketplace."""
    try:
        client = MarketplaceClient(index_url)
        results = client.search(query)

        if not results:
            console.print(f"No plugins found matching '{query}'.")
            return

        table = Table(title="Search Results")
        table.add_column("Name", style="cyan")
        table.add_column("Description", style="magenta")
        table.add_column("Signed", style="green")

        for p in results:
            signed = "Yes" if p.get("signature") else "No"
            table.add_row(p.get("name", ""), p.get("description", ""), signed)

        console.print(table)
    except Exception as e:
        console.print(f"[bold red]Error searching marketplace: {e}[/bold red]")
        raise typer.Exit(1)


@app.command("install")
def install(
    name: str,
    target_dir: str = "plugins",
    public_key_path: Optional[str] = None,
    index_url: str = DEFAULT_INDEX_URL,
) -> None:
    """Install a plugin from the marketplace."""
    try:
        pub_pem = None
        if public_key_path:
            with open(public_key_path, "rb") as f:
                pub_pem = f.read()
        else:
            from pathlib import Path

            bundled_key_path = (
                Path(__file__).parent.parent / "sdk" / "ecosystem" / "public_key.pem"
            )
            if bundled_key_path.exists():
                with open(bundled_key_path, "rb") as f:
                    pub_pem = f.read()

        client = MarketplaceClient(index_url)
        with console.status(f"Installing {name}..."):
            install_path = client.install_plugin(name, target_dir, pub_pem)

        console.print(
            f"[bold green]Successfully installed {name} to {install_path}[/bold green]"
        )
    except Exception as e:
        console.print(f"[bold red]Error installing plugin: {e}[/bold red]")
        raise typer.Exit(1)
