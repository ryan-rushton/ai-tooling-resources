# Project-Specific Agent Instructions

<!--
HOW TO USE THIS TEMPLATE:

When initializing this file for a new project:
1. Read the codebase first - explore README, package files, directory structure, existing code
2. Fill out each section using the exploration guidance provided in the comments
3. Remove the comment blocks after filling out each section
4. Keep the defaults for Testing Philosophy, Visibility and Encapsulation, and Documentation (they're universal best practices)
5. If you're unsure about something, follow the "ask" prompts to get clarification from the user
6. Prioritize being concise - document what's necessary, not everything possible
7. Use bulleted lists and code blocks for clarity

The goal is to create a reference document that helps future AI assistants (and human developers) quickly understand:
- What this project does
- How to work with the codebase
- Where to find things
- What patterns and conventions to follow
-->

This file contains repository-specific guidance for AI coding tools.

## Project Overview

<!--
When filling this out:
1. Read the README.md, package.json/pyproject.toml/pom.xml, or similar entry files
2. Provide a 2-3 sentence description of the project's purpose
3. If unclear, ask the user: "What is the primary purpose of this project?"
-->

### Tech Stack

<!--
List key technologies, frameworks, and languages used.
Explore: Look at dependency files (package.json, requirements.txt, Gemfile, etc.)
Include: Language version, major frameworks, build tools, test frameworks
-->

### Architecture

<!--
Describe the high-level architecture in 2-4 bullet points.
Explore: Review directory structure, main entry points, and module organization
If the architecture is non-obvious, ask: "What's the high-level architecture approach?" (e.g., microservices, monolith, layered, event-driven)
-->

## Development Workflow

### Building

<!--
Explore: Look for build scripts in package.json, Makefile, build.gradle, pyproject.toml
List the specific commands to build/compile the project
Examples: "npm run build", "mvn package", "cargo build", "uv build"
-->

### Testing

#### Testing Philosophy

- **Black box testing** - Test behavior, not implementation details
- **Succinct tests** - Keep tests focused and readable
- **Group related conditions** - Test related scenarios together in a single test when it makes sense
- **Separate code paths** - Create distinct tests for alternative flows and edge cases

#### Test Organization

- Group tests by class/module → method/function → scenario
- Use prefixes on test names or nested describe blocks depending on language conventions
- Explore existing tests to understand the project's organization pattern

#### Running Tests

<!--
Explore: Look for test scripts in package.json, Makefile, pytest.ini, or CI config files
List the specific commands to run tests
Include options for: all tests, specific test files, with coverage
Examples: "npm test", "pytest tests/", "mvn test", "cargo test"
-->

### Linting and Formatting

<!--
Explore: Look for linting config files (.eslintrc, .ruff.toml, pyproject.toml, etc.) and format scripts
List the specific commands to lint and format code
Examples: "npm run lint", "ruff check src/", "cargo clippy", "mvn checkstyle:check"
Linting and formatting should be treated as the last step when writing coding features if available
-->

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

<!--
Explore: Review existing code to identify naming patterns otherwise use community standards and conventions as the default
Document in bulleted list format. Common patterns to look for:
- Function/method naming: snake_case (Python), camelCase (JS/Java/Go), PascalCase (C#)
- Class naming: PascalCase in most languages
- Constant naming: UPPER_SNAKE_CASE in most languages
- Private/internal indicators: underscore prefix (_method), # for JS private fields, private keyword
- Variable naming: match function convention

Example documentation:
- Python: `snake_case` for functions/variables, `PascalCase` for classes
- Private methods: prefix with underscore (`_method_name`)
- Constants: `UPPER_SNAKE_CASE`

If patterns are inconsistent, ask: "What naming conventions should be followed?"
-->

## Common Tasks

### Adding New Features

<!--
Document the step-by-step process for adding features as a numbered list.
If there's a CONTRIBUTING.md file, reference or summarize it.
Otherwise, infer from the codebase and CI configuration. Common steps to consider:
1. Branch creation (if using git flow)
2. Where to add code (module/directory structure)
3. Code requirements (type hints, documentation, etc.)
4. Testing requirements (write tests first? test location? coverage requirements?)
5. Documentation updates (README, API docs, changelogs)
6. Quality checks to run (linting, type checking, tests)
7. Review process (PR requirements, approval needed?)

Example documentation:
1. Add command to `src/ai_tooling/cli.py` with `@main.command()` decorator
2. Implement logic in appropriate module (or create new module in `src/ai_tooling/`)
3. Add comprehensive type hints - must pass `mypy --strict`
4. Write tests in `tests/test_<module>.py` following black box testing approach
5. Update README.md with command documentation and examples
6. Run all checks: `uv run ruff check src/ && uv run mypy src/ && uv run pytest tests/`

If unclear, ask: "What's the process for adding new features?"
-->

### Debugging

- Debugging should be primarily done via writing unit tests or integration tests where possible
- A last resort, particularly for complex browser interactions and such can be to use print statements and ask the user to copy them for you

### Dependencies

<!--
Explore: Identify the package manager and dependency files
- JavaScript/TypeScript: package.json → npm/yarn/pnpm/bun
- Python: requirements.txt/pyproject.toml/setup.py → pip/poetry/uv/pipenv
- Rust: Cargo.toml → cargo
- Java: pom.xml/build.gradle → maven/gradle
- Go: go.mod → go
- Ruby: Gemfile → bundler

Document as bulleted list with specific commands. Include:
- Add production dependency
- Add development dependency
- Update dependencies
- Remove dependency
- Install all dependencies (for new contributors)
- Lock file management (if applicable)

Example documentation:
- Add dependencies: `uv add <package>` (adds to `[project.dependencies]`)
- Add dev dependencies: `uv add --dev <package>` (adds to `[project.optional-dependencies.dev]`)
- Sync after changes: `uv sync`
- Build package: `uv build`
-->

## Project-Specific Patterns

<!--
Document unique patterns, conventions, or gotchas as bulleted list with bold labels.
Explore the codebase for unusual patterns. Look for:
- Custom abstractions: decorators, middleware, base classes, mixins, traits
- Architectural patterns: plugin systems, event sourcing, CQRS, microservices conventions
- Data flow patterns: how state is managed, how data moves through the system
- Performance patterns: caching strategies, lazy loading, memoization
- Security patterns: authentication flows, authorization checks, input validation
- Naming patterns: specific prefixes/suffixes with meaning (e.g., *Service, *Repository, use*)
- File organization patterns: where different types of code live
- Testing patterns: fixtures, mocks, test data generation
- Common gotchas: things that trip up new contributors

Example documentation:
- **Metadata tracking**: Section hashes stored in `.ai-tooling/{filename}.meta.json` files
- **Symlinks for project files**: `AGENTS.md` is source, `CLAUDE.md` and `GEMINI.md` are symlinks
- **Section parsing**: Only H2 headers (`## `) are tracked, not H3 or deeper
- **Path expansion**: Always use `expand_path()` from utils to handle `~` in paths
- **Type annotations after JSON**: Annotate variables after `json.loads()` for mypy strictness

If nothing stands out, leave this section empty or ask: "Are there any project-specific patterns I should know about?"
-->

## Additional Notes

<!-- Add project-specific notes below this line -->
