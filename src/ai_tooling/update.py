"""Update logic for AI tooling configuration files."""

from pathlib import Path

import click

from ai_tooling.install import get_repo_root, load_tool_mappings
from ai_tooling.utils import (
    compute_section_hash,
    expand_path,
    load_metadata,
    parse_markdown_sections,
    print_header,
    print_info,
    print_success,
    print_warning,
    update_metadata_hash,
)


def replace_section_in_file(file_path: Path, section_name: str, new_content: str) -> None:
    """Replace a section in a markdown file with new content."""
    if not file_path.exists():
        return

    content = file_path.read_text()
    lines = content.split("\n")
    new_lines = []
    in_target_section = False
    section_header = f"## {section_name}"

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check if this is the start of our target section
        if line == section_header:
            in_target_section = True
            # Add the section header and new content
            new_lines.append(section_header)
            new_lines.extend(new_content.split("\n"))

            # Skip to next section or H1
            i += 1
            while i < len(lines):
                next_line = lines[i]
                # Stop at next H2 or H1
                if next_line.startswith("## ") or next_line.startswith("# "):
                    break
                i += 1
            in_target_section = False
            continue

        # Keep lines that aren't in the target section
        if not in_target_section:
            new_lines.append(line)

        i += 1

    file_path.write_text("\n".join(new_lines))


def update_file(
    target_path: str, template_name: str, dry_run: bool = False
) -> tuple[int, int, list[str]]:
    """
    Update a configuration file, preserving user modifications.

    Returns:
        Tuple of (updated_sections, skipped_sections, skipped_names)
    """
    target = expand_path(target_path)

    # Check if target exists
    if not target.exists():
        print_warning(f"Target file not found: {target} (skipping)")
        return 0, 0, []

    # Check if metadata exists
    metadata = load_metadata(target)
    if metadata is None:
        print_warning(f"No metadata found for {target} (skipping - was it installed manually?)")
        return 0, 0, []

    print_info(f"Checking {target}...")

    repo_root = get_repo_root()
    template_file = repo_root / "templates" / template_name

    if not template_file.exists():
        print_warning(f"Template not found: {template_file}")
        return 0, 0, []

    # Parse both files
    template_sections = parse_markdown_sections(template_file)
    current_sections = parse_markdown_sections(target)

    updated_count = 0
    skipped_count = 0
    skipped_names = []

    for section_name, template_content in template_sections.items():
        # Get original hash from metadata
        original_hash = metadata.get("sections", {}).get(section_name)

        if original_hash is None:
            # New section in template
            print_info(f"  New section found: {section_name}")
            continue

        # Compute current hash
        current_content = current_sections.get(section_name, "")
        current_hash = compute_section_hash(current_content)

        if current_hash == original_hash:
            # Section unchanged, update it
            if dry_run:
                print_success(f"  Would update: {section_name}")
                updated_count += 1
            else:
                replace_section_in_file(target, section_name, template_content)
                # Update metadata with new hash
                new_hash = compute_section_hash(template_content)
                update_metadata_hash(target, section_name, new_hash)
                updated_count += 1
        else:
            # Section modified by user, skip it
            skipped_count += 1
            skipped_names.append(section_name)

    return updated_count, skipped_count, skipped_names


def update_global_files(dry_run: bool = False) -> None:
    """Update global configuration files."""
    print_header("Checking global configuration files...")

    config = load_tool_mappings()

    for _tool_name, tool_config in config["tools"].items():
        if not tool_config.get("enabled", True):
            continue

        global_config = tool_config.get("global")
        if not global_config or not global_config.get("path"):
            continue

        template = global_config["source_template"]
        target_path = global_config["path"]

        updated, skipped, skipped_names = update_file(target_path, template, dry_run)

        if updated > 0:
            if dry_run:
                print_info(f"Would update {updated} section(s) in {expand_path(target_path)}")
            else:
                print_success(f"Updated {updated} section(s) in {expand_path(target_path)}")

        if skipped > 0:
            skipped_list = "\n    - ".join(skipped_names)
            print_warning(f"Skipped {skipped} modified section(s):\n    - {skipped_list}")

        click.echo()


def update_local_files(project_dir: str | None = None, dry_run: bool = False) -> None:
    """Update project-specific configuration files.

    Only updates AGENTS.md since CLAUDE.md and GEMINI.md are symlinks to it.
    """
    if project_dir is None:
        project_dir = "."

    project_path = expand_path(project_dir)

    print_header(f"Checking project configuration files in {project_path}...")

    # Only update AGENTS.md - the symlinks (CLAUDE.md, GEMINI.md) will reflect changes automatically
    agents_path = project_path / "AGENTS.md"

    updated, skipped, skipped_names = update_file(str(agents_path), "PROJECT.md", dry_run)

    if updated > 0:
        if dry_run:
            print_info(f"Would update {updated} section(s) in {agents_path}")
        else:
            print_success(f"Updated {updated} section(s) in {agents_path}")
        print_info("Symlinks (CLAUDE.md, GEMINI.md) will reflect these changes automatically")

    if skipped > 0:
        skipped_list = "\n    - ".join(skipped_names)
        print_warning(f"Skipped {skipped} modified section(s):\n    - {skipped_list}")

    click.echo()


def run_update(scope: str = "both", project_dir: str | None = None, dry_run: bool = False) -> None:
    """
    Run update based on scope.

    Args:
        scope: "global", "local", or "both"
        project_dir: Project directory for local updates
        dry_run: If True, show what would be updated without making changes
    """
    if dry_run:
        print_info("DRY RUN MODE - No files will be modified")
        click.echo()

    if scope in ("global", "both"):
        update_global_files(dry_run)

    if scope in ("local", "both"):
        update_local_files(project_dir, dry_run)

    print_header("Update Complete!")

    if dry_run:
        click.echo()
        print_info("This was a dry run. Run without --dry-run to apply updates.")
