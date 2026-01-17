"""Tests for utility functions."""

from pathlib import Path

from ai_tooling.utils import compute_section_hash, parse_markdown_sections


def test_compute_section_hash():
    """Test section hash computation."""
    content1 = "This is a test"
    content2 = "This is a test"
    content3 = "Different content"

    hash1 = compute_section_hash(content1)
    hash2 = compute_section_hash(content2)
    hash3 = compute_section_hash(content3)

    assert hash1 == hash2
    assert hash1 != hash3


def test_parse_markdown_sections(tmp_path):
    """Test parsing markdown file into sections."""
    test_file = tmp_path / "test.md"
    content = """# Main Title

Some intro text

## Section One

Content for section one
More content

## Section Two

Content for section two

## Section Three

Final section
"""
    test_file.write_text(content)

    sections = parse_markdown_sections(test_file)

    assert len(sections) == 3
    assert "Section One" in sections
    assert "Section Two" in sections
    assert "Section Three" in sections

    assert "Content for section one" in sections["Section One"]
    assert "Content for section two" in sections["Section Two"]
    assert "Final section" in sections["Section Three"]


def test_parse_markdown_sections_nonexistent_file():
    """Test parsing a non-existent file returns empty dict."""
    sections = parse_markdown_sections(Path("/nonexistent/file.md"))
    assert sections == {}
