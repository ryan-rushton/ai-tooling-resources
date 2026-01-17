"""CLI for ai-tooling - Unified configuration system for AI coding tools."""

import click

from ai_tooling import __version__


@click.group()
@click.version_option(version=__version__)
def main() -> None:
    """AI Tooling - Unified configuration system for AI coding tools."""
    pass


@main.command()
@click.option("--global", "is_global", is_flag=True, help="Install only global configuration files")
@click.option(
    "--local", "is_local", is_flag=True, help="Install only local/project configuration files"
)
@click.option(
    "--project-dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="Project directory for local installation (default: current directory)",
)
def install(is_global: bool, is_local: bool, project_dir: str | None) -> None:
    """Install AI tool configuration files."""
    from ai_tooling.install import run_install

    if is_global and is_local:
        click.echo("Error: Cannot specify both --global and --local", err=True)
        raise click.Abort()

    # Determine install type
    if is_global:
        install_type = "global"
    elif is_local:
        install_type = "local"
    else:
        install_type = "both"

    run_install(install_type=install_type, project_dir=project_dir)


@main.command()
@click.option("--global", "is_global", is_flag=True, help="Update only global configuration files")
@click.option(
    "--local", "is_local", is_flag=True, help="Update only local/project configuration files"
)
@click.option(
    "--project-dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="Project directory for local updates (default: current directory)",
)
@click.option("--dry-run", is_flag=True, help="Show what would be updated without making changes")
def update(is_global: bool, is_local: bool, project_dir: str | None, dry_run: bool) -> None:
    """Update AI tool configuration files (preserves user modifications)."""
    from ai_tooling.update import run_update

    if is_global and is_local:
        click.echo("Error: Cannot specify both --global and --local", err=True)
        raise click.Abort()

    # Determine update scope
    if is_global:
        update_scope = "global"
    elif is_local:
        update_scope = "local"
    else:
        update_scope = "both"

    run_update(scope=update_scope, project_dir=project_dir, dry_run=dry_run)


@main.command("self-update")
def self_update() -> None:
    """Update the ai-tooling CLI itself to the latest version."""
    import subprocess

    from ai_tooling.install import get_repo_root

    try:
        repo_root = get_repo_root()
    except RuntimeError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort() from e

    click.echo("Updating ai-tooling CLI...")

    # Pull latest changes
    try:
        result = subprocess.run(
            ["git", "pull", "--ff-only"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True,
        )
        click.echo(result.stdout)

        # Reinstall dependencies
        click.echo("Reinstalling dependencies...")
        subprocess.run(["uv", "sync"], cwd=repo_root, check=True, capture_output=True)

        click.secho("✓ ai-tooling CLI updated successfully!", fg="green")
        click.echo("\nRun 'ai-tooling update' to update your configuration files.")

    except subprocess.CalledProcessError as e:
        click.echo(f"Error updating: {e.stderr}", err=True)
        raise click.Abort() from e
    except FileNotFoundError as e:
        click.echo(f"Error: Required command not found ({e.filename})", err=True)
        raise click.Abort() from e


if __name__ == "__main__":
    main()
