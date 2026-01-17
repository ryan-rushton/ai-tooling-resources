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
    install_dir = expand_path("~/.ai-tooling")
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
    """Install project-specific configuration files.

    Installs AGENTS.md as the source file, then creates CLAUDE.md and GEMINI.md as symlinks.
    """
    if project_dir is None:
        project_dir = "."

    project_path = expand_path(project_dir)

    print_header(f"Installing project configuration files to {project_path}...")

    # Install AGENTS.md as the main file
    repo_root = get_repo_root()
    agents_template = repo_root / "templates" / "PROJECT.md"
    agents_target = project_path / "AGENTS.md"

    if not agents_template.exists():
        raise FileNotFoundError(f"Template not found: {agents_template}")

    agents_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(agents_template, agents_target)
    print_success(f"Installed: {agents_target}")

    # Create metadata for AGENTS.md
    sections = parse_markdown_sections(agents_target)
    create_metadata(agents_target, sections)

    # Create symlinks for CLAUDE.md and GEMINI.md
    claude_target = project_path / "CLAUDE.md"
    gemini_target = project_path / "GEMINI.md"

    # Remove existing files/symlinks if they exist
    if claude_target.exists() or claude_target.is_symlink():
        claude_target.unlink()
    if gemini_target.exists() or gemini_target.is_symlink():
        gemini_target.unlink()

    # Create symlinks (relative to make them portable)
    claude_target.symlink_to("AGENTS.md")
    print_success(f"Created symlink: {claude_target} -> AGENTS.md")

    gemini_target.symlink_to("AGENTS.md")
    print_success(f"Created symlink: {gemini_target} -> AGENTS.md")

    click.echo()


def install_feature_file(target_dir: str | None = None, file_name: str = "AGENTS.md") -> None:
    """Install a feature-specific instruction file.

    Args:
        target_dir: Directory to install the feature file (default: current directory)
        file_name: Name for the feature file (default: AGENTS.md)
    """
    if target_dir is None:
        target_dir = "."

    target_path = expand_path(target_dir)

    if not target_path.exists():
        click.echo(f"Error: Directory does not exist: {target_path}", err=True)
        raise click.Abort()

    print_header(f"Initializing feature-specific instructions in {target_path}...")

    # Get the template
    repo_root = get_repo_root()
    feature_template = repo_root / "templates" / "FEATURE.md"

    if not feature_template.exists():
        raise FileNotFoundError(f"Template not found: {feature_template}")

    # Target file
    target_file = target_path / file_name

    if target_file.exists():
        click.echo(f"Warning: {target_file} already exists", err=True)
        if not click.confirm("Overwrite?"):
            click.echo("Aborted.")
            raise click.Abort()

    # Copy template to target
    target_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(feature_template, target_file)
    print_success(f"Created: {target_file}")

    # Create metadata for tracking
    sections = parse_markdown_sections(target_file)
    create_metadata(target_file, sections)

    click.echo()
    print_success("Feature file initialized!")
    click.echo()
    click.echo("Next steps:")
    click.echo(f"  1. Edit {target_file} to document this feature/module")
    click.echo("  2. Remove comment blocks as you fill out each section")
    click.echo("  3. Run 'ai-tooling update --local' later to update from template changes")


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
        click.echo("  - AGENTS.md        (source file - Cursor + Codex)")
        click.echo("  - CLAUDE.md -> AGENTS.md   (symlink)")
        click.echo("  - GEMINI.md -> AGENTS.md   (symlink)")
        click.echo()
        click.echo("Note: All AI tools use the same AGENTS.md file via symlinks")
        click.echo()

    print_success("Installation complete!")
    click.echo()
    click.echo("Next steps:")
    click.echo("  1. Review and customize the installed configuration files")
    click.echo("  2. Run 'ai-tooling update' to check for updates later")
    click.echo("  3. Use 'ai-tooling init-feature --dir <path>' for feature-specific instructions")
