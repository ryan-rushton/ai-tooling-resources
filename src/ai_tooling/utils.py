"""Utility functions for AI tooling."""

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

import click


def expand_path(path: str) -> Path:
    """Expand ~ and environment variables in path."""
    return Path(path).expanduser().resolve()


def compute_section_hash(content: str) -> str:
    """Compute SHA256 hash of section content."""
    return hashlib.sha256(content.encode()).hexdigest()


def parse_markdown_sections(file_path: Path) -> dict[str, str]:
    """
    Parse markdown file into sections based on H2 headers (##).

    Returns dict mapping section names to their content (excluding the header itself).
    """
    if not file_path.exists():
        return {}

    content = file_path.read_text()
    sections: dict[str, str] = {}
    current_section: str | None = None
    current_content: list[str] = []

    for line in content.split("\n"):
        # Check for H2 header (## heading)
        if re.match(r"^## \w", line):
            # Save previous section
            if current_section is not None:
                sections[current_section] = "\n".join(current_content)

            # Start new section
            current_section = line[3:].strip()  # Remove "## "
            current_content = []
        elif current_section is not None:
            current_content.append(line)

    # Save final section
    if current_section is not None:
        sections[current_section] = "\n".join(current_content)

    return sections


def create_metadata(target_file: Path, sections: dict[str, str]) -> None:
    """Create metadata file tracking section hashes."""
    metadata = {
        "version": "1.0.0",
        "installed_at": datetime.utcnow().isoformat() + "Z",
        "source_repo": "ai-tooling-resources",
        "sections": {name: compute_section_hash(content) for name, content in sections.items()},
    }

    metadata_file = target_file.with_suffix(target_file.suffix + ".ai-tooling-meta.json")
    metadata_file.write_text(json.dumps(metadata, indent=2))


def load_metadata(target_file: Path) -> dict[str, Any] | None:
    """Load metadata file if it exists."""
    metadata_file = target_file.with_suffix(target_file.suffix + ".ai-tooling-meta.json")
    if not metadata_file.exists():
        return None

    try:
        data: dict[str, Any] = json.loads(metadata_file.read_text())
        return data
    except (json.JSONDecodeError, OSError):
        return None


def update_metadata_hash(target_file: Path, section_name: str, new_hash: str) -> None:
    """Update the hash for a specific section in metadata."""
    metadata_file = target_file.with_suffix(target_file.suffix + ".ai-tooling-meta.json")
    if not metadata_file.exists():
        return

    try:
        metadata = json.loads(metadata_file.read_text())
        metadata["sections"][section_name] = new_hash
        metadata_file.write_text(json.dumps(metadata, indent=2))
    except (json.JSONDecodeError, OSError, KeyError):
        pass


def print_success(message: str) -> None:
    """Print success message with checkmark."""
    click.secho(f"✓ {message}", fg="green")


def print_warning(message: str) -> None:
    """Print warning message."""
    click.secho(f"⚠ {message}", fg="yellow")


def print_info(message: str) -> None:
    """Print info message."""
    click.secho(f"ℹ {message}", fg="blue")


def print_header(message: str) -> None:
    """Print header message."""
    click.secho(message, fg="blue", bold=True)
