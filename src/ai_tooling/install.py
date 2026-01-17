"""Installation logic for AI tooling configuration files."""

import json
import shutil
from pathlib import Path
from typing import Any

import click

from ai_tooling.utils import (
    create_metadata,
    expand_path,
    parse_markdown_sections,
    print_header,
    print_success,
)


def get_repo_root() -> Path:
    """Get the repository root directory."""
    # When installed via pip, we need to find the templates
    # Check if we're in development mode first
    current_file = Path(__file__).resolve()
    repo_root = current_file.parent.parent.parent

    templates_dir = repo_root / "templates"
    if templates_dir.exists():
        return repo_root

    # If not in dev mode, check install directory
    install_dir = expand_path("~/.ai-tooling-resources")
    if install_dir.exists():
        return install_dir

    raise RuntimeError("Could not find AI tooling resources. Run bootstrap.sh first.")


def load_tool_mappings() -> dict[str, Any]:
    """Load tool mappings configuration."""
    repo_root = get_repo_root()
    config_file = repo_root / "config" / "tool-mappings.json"

    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_file}")

    data: dict[str, Any] = json.loads(config_file.read_text())
    return data


def install_file(template_name: str, target_path: str) -> None:
    """Install a configuration file from template."""
    repo_root = get_repo_root()
    template_file = repo_root / "templates" / template_name

    if not template_file.exists():
        raise FileNotFoundError(f"Template not found: {template_file}")

    target = expand_path(target_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    # Copy template to target
    shutil.copy2(template_file, target)
    print_success(f"Installed: {target}")

    # Create metadata for tracking
    sections = parse_markdown_sections(target)
    create_metadata(target, sections)


def install_global_files() -> None:
    """Install global configuration files."""
    print_header("Installing global configuration files...")

    config = load_tool_mappings()

    for _tool_name, tool_config in config["tools"].items():
        if not tool_config.get("enabled", True):
            continue

        global_config = tool_config.get("global")
        if not global_config or not global_config.get("path"):
            continue

        template = global_config["source_template"]
        target_path = global_config["path"]

        install_file(template, target_path)

    click.echo()


def install_local_files(project_dir: str | None = None) -> None:
    """Install project-specific configuration files."""
    if project_dir is None:
        project_dir = "."

    project_path = expand_path(project_dir)

    print_header(f"Installing project configuration files to {project_path}...")

    config = load_tool_mappings()

    for _tool_name, tool_config in config["tools"].items():
        if not tool_config.get("enabled", True):
            continue

        project_config = tool_config.get("project")
        if not project_config or not project_config.get("path"):
            continue

        template = project_config["source_template"]
        target_filename = project_config["path"]
        target_path = project_path / target_filename

        install_file(template, str(target_path))

    click.echo()


def run_install(install_type: str = "both", project_dir: str | None = None) -> None:
    """
    Run installation based on type.

    Args:
        install_type: "global", "local", or "both"
        project_dir: Project directory for local installation
    """
    if install_type in ("global", "both"):
        install_global_files()

    if install_type in ("local", "both"):
        install_local_files(project_dir)

    print_header("Installation Summary")
    click.echo()
    click.echo("Global files installed:")
    click.echo("  - Claude Code:  ~/.claude/CLAUDE.md")
    click.echo("  - Gemini:       ~/.gemini/GEMINI.md")
    click.echo("  - Codex:        ~/.codex/AGENTS.md")
    click.echo()

    if install_type in ("local", "both"):
        project_path = expand_path(project_dir or ".")
        click.echo(f"Project files installed to {project_path}:")
        click.echo("  - CLAUDE.md   (Claude Code)")
        click.echo("  - GEMINI.md   (Gemini Code Assist)")
        click.echo("  - AGENTS.md   (Cursor + Codex)")
        click.echo()

    print_success("Installation complete!")
    click.echo()
    click.echo("Next steps:")
    click.echo("  1. Review and customize the installed configuration files")
    click.echo("  2. Run 'ai-tooling update' to check for updates later")
