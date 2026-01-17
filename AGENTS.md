# Project-Specific Agent Instructions

This file contains repository-specific guidance for AI coding tools.

## Project Overview

Unified configuration system for AI-powered coding tools. Provides templates and a CLI for managing configuration files (AGENTS.md, CLAUDE.md, GEMINI.md) across global and project-specific installations. The philosophy is that AI tools are commodities - this system makes it seamless to swap between Claude, Gemini, Cursor, Codex, etc.

### Tech Stack

- **Python 3.10+** - CLI implementation
- **uv** - Fast Python package manager
- **Click** - CLI framework
- **pytest** - Testing framework
- **ruff** - Linter and formatter
- **mypy** - Static type checker (strict mode)
- **Prettier** - Markdown and JSON formatter

### Architecture

- **Templates** (`templates/`) - Markdown templates for AI tool configurations
  - `GLOBAL.md` - Meta-behavioral preferences template
  - `PROJECT.md` - Project-level instructions template
  - `FEATURE.md` - Feature/module-specific instructions template
- **CLI** (`src/ai_tooling/`) - Python package with Click-based CLI
  - `cli.py` - Command definitions (install, update, init-feature, self-update)
  - `install.py` - Installation logic with symlink creation and feature file initialization
  - `update.py` - Update logic with section-based change tracking
  - `utils.py` - Shared utilities (hashing, file operations, colored output)
- **Scripts** (`scripts/bootstrap.sh`) - Curl-able bootstrap script for one-line installation
- **Config** (`config/tool-mappings.json`) - Tool configuration mappings
- **Metadata** (`.ai-tooling/`) - Section hash tracking for preserving user modifications

## Development Workflow

### Building

```bash
# Install dependencies
uv sync --all-extras

# Build the package (creates wheel and sdist in dist/)
uv build

# Run the CLI locally without installing
uv run ai-tooling --help
```

### Testing

#### Testing Philosophy

- **Black box testing** - Test behavior, not implementation details
- **Succinct tests** - Keep tests focused and readable
- **Group related conditions** - Test related scenarios together in a single test when it makes sense
- **Separate code paths** - Create distinct tests for alternative flows and edge cases

#### Test Organization

- Group tests by class/module → method/function → scenario
- Use prefixes on test names or nested describe blocks depending on language conventions
- See tests/ directory for examples of this project's organization pattern

#### Running Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=src/ai_tooling --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_utils.py -v
```

### Linting and Formatting

```bash
# Linting
uv run ruff check src/

# Formatting
uv run ruff format src/

# Type checking
uv run mypy src/

# Format markdown and JSON (using Prettier via VS Code extension)
# Save files in VS Code with format-on-save enabled, or run:
# npx prettier --write "**/*.md" "**/*.json"

# Fix auto-fixable linting issues
uv run ruff check --fix src/

# Run all checks (recommended before committing)
uv run ruff check src/ && uv run ruff format src/ && uv run mypy src/ && uv run pytest tests/
```

## Code Standards

### Visibility and Encapsulation

- Keep methods private/internal by default - only expose what's necessary
- Avoid exposing internals just for testing - reconsider the design instead
- Each class should have a minimal public interface with one clear purpose
- Prefer single responsibility - typically one primary public method per class

### Documentation

- Explain the purpose, not the implementation
- Keep docstrings focused on what and why, not how
- Document behavior: what it does, what it returns, edge cases
- Avoid verbose examples in docstrings

### Naming Conventions

- Python: `snake_case` for functions/variables, `PascalCase` for classes
- Private methods: prefix with underscore (`_method_name`)
- Constants: `UPPER_SNAKE_CASE`

### Error Handling

- Use exceptions for error conditions - raise specific exception types
- Chain exceptions with `from e` when re-raising (required by ruff B904)
- CLI commands should catch exceptions and use `click.Abort()` for user-facing errors
- Include helpful error messages that guide users to solutions

### Logging

- Use `click.echo()` for standard output in CLI commands
- Use colored output helpers from `utils.py`: `print_success()`, `print_warning()`, `print_info()`, `print_header()`
- Keep output concise - users should see progress without noise

## Common Tasks

### Adding New CLI Commands

1. Add command to `src/ai_tooling/cli.py` with `@main.command()` decorator
1. Implement logic in appropriate module (or create new module in `src/ai_tooling/`)
1. Add comprehensive type hints - must pass `mypy --strict`
1. Write tests in `tests/test_<module>.py` following black box testing approach
1. Update README.md with command documentation and examples
1. Run all checks: `uv run ruff check src/ && uv run mypy src/ && uv run pytest tests/`

### Creating Feature-Specific Instructions

Use `ai-tooling init-feature` to add context for a specific feature/module:

```bash
# Create AGENTS.md in a feature directory
ai-tooling init-feature --dir src/authentication

# Use custom filename
ai-tooling init-feature --dir lib/payments --name PAYMENTS.md

# Update later if template changes
ai-tooling update --local --project-dir src/authentication
```

### Debugging

- Run CLI directly: `uv run ai-tooling <command> --help`
- Run tests with verbose output: `uv run pytest tests/ -vv`
- Use `--dry-run` flag on update command to preview changes
- Check metadata files in `.ai-tooling/` to debug section tracking

### Dependencies

- Add dependencies: `uv add <package>` (adds to `[project.dependencies]`)
- Add dev dependencies: `uv add --dev <package>` (adds to `[project.optional-dependencies.dev]`)
- Sync after changes: `uv sync`
- Build package: `uv build`

## Project-Specific Patterns

- **Metadata tracking**: Section hashes stored in `.ai-tooling/{filename}.meta.json` files
- **Symlinks for project files**: `AGENTS.md` is source, `CLAUDE.md` and `GEMINI.md` are symlinks
- **Section parsing**: Only H2 headers (`## `) are tracked, not H3 or deeper
- **Path expansion**: Always use `expand_path()` from utils to handle `~` in paths
- **Type annotations after JSON**: Annotate variables after `json.loads()` for mypy strictness
- **Feature-level instructions**: Use `ai-tooling init-feature` to create AGENTS.md files in subdirectories for feature/module-specific context that supplements the project-level AGENTS.md

---

_This file is managed by [ai-tooling](https://github.com/ryan-rushton/ai-tooling). Customize sections below this line._

## Additional Notes

### Key Design Decisions

**Template Section Tracking:**

- Templates use H2 headers (`##`) as the basis for update tracking
- Metadata stored in `.ai-tooling/` directory as `{filename}.meta.json`
- SHA256 hashes track each section independently
- User modifications are preserved during updates

**Symlink Strategy for Project Files:**

- `AGENTS.md` is the source file
- `CLAUDE.md` and `GEMINI.md` are symlinks to `AGENTS.md`
- Philosophy: AI tools are commodities, seamlessly swap between them
- Only one metadata file needed since all tools use the same content

**Type Safety:**

- All code must pass `mypy --strict`
- Use `dict[str, Any]` for JSON data
- Annotate variables after `json.loads()` to satisfy mypy

### Testing Strategy

- Focus on black box testing through public CLI commands
- Test utility functions (hashing, markdown parsing)
- Keep tests succinct and focused on behavior
- Test files in `tests/` directory matching `test_*.py` pattern

### Common Workflows

**Making Template Changes:**

1. Edit `templates/GLOBAL.md` or `templates/PROJECT.md`
1. Format with Prettier (save in VS Code or run `npx prettier --write templates/*.md`)
1. Test locally: `uv run ai-tooling install --local --project-dir .`
1. Verify update preserves user changes: add custom section, run update --dry-run
1. Run all checks before committing

**Adding a New CLI Command:**

1. Add command to `src/ai_tooling/cli.py` with `@main.command()` decorator
1. Implement logic in appropriate module (or create new one)
1. Add type hints everywhere
1. Add tests in `tests/test_<module>.py`
1. Update README.md with command documentation
1. Run: `uv run mypy src/ && uv run pytest tests/ && uv run ruff check src/`
