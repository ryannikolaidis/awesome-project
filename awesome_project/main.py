"""Command-line interface for awesome-project."""

import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer(
    name="awesome-project",
    help="A Python project called awesome-project",
    add_completion=False,
)
console = Console()


@app.command()
def hello(
    name: str = typer.Option("World", "--name", "-n", help="Name to greet"),
    loud: bool = typer.Option(False, "--loud", "-l", help="Shout the greeting"),
) -> None:
    """Say hello to someone."""
    greeting = f"Hello {name}!"
    if loud:
        greeting = greeting.upper()

    console.print(Panel.fit(greeting, style="green"))


@app.command()
def info() -> None:
    """Show information about awesome-project."""
    from . import __version__

    info_text = f"""[bold blue]awesome-project[/bold blue]

[bold]Version:[/bold] {__version__}
[bold]Description:[/bold] A Python project called awesome-project

[dim]Add your application logic here![/dim]"""

    console.print(Panel(info_text, title="📋 Application Info", expand=False))


@app.command()
def config(
    show: bool = typer.Option(False, "--show", help="Show current configuration"),
) -> None:
    """Manage application configuration."""
    if show:
        console.print("[yellow]No configuration file found.[/yellow]")
        console.print("[dim]Add your configuration logic here![/dim]")
    else:
        console.print("[green]Configuration created![/green]")
        console.print("[dim]Add your configuration setup logic here![/dim]")


def main() -> None:
    """Entry point for the CLI application."""
    app()


if __name__ == "__main__":
    main()
