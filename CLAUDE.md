# CLAUDE.md

This repository provides a unified configuration system for AI coding tools.

## Repository Purpose

This is a **template and script repository** for managing AI tool configuration files. It contains:

- **Templates**: `GLOBAL.md` and `AGENTS.md` templates for AI tool instructions
- **Scripts**: Installation and update scripts for managing config files
- **Config**: Tool mappings for Claude Code, Gemini, Cursor, and Codex

This repository has **no code to execute** - it's purely for documentation and scripts.

## Working with This Repository

When making changes to this repository, focus on:

1. **Templates** (`templates/*.md`): These are the source templates that get copied to user systems
1. **Scripts** (`scripts/*.sh`): Bash scripts for install/update functionality
1. **Config** (`config/tool-mappings.json`): Tool configuration metadata
1. **README.md**: User-facing documentation

## Important Notes

- The templates use markdown section headers (##) as the basis for update tracking
- Any changes to section headers in templates may affect the update script's behavior
- The install script creates `.ai-tooling-meta.json` files to track section hashes
- Scripts should remain POSIX-compliant for maximum compatibility

## Testing Changes

When modifying scripts:

1. Test the install script in a clean environment
1. Test the update script with both modified and unmodified sections
1. Verify metadata files are created correctly
1. Check that the bootstrap script works with curl
