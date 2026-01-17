# AI Tooling

A unified configuration system for AI-powered coding tools. Manage global and project-specific instructions for Claude Code, Gemini Code Assist, Cursor, and OpenAI Codex from a single source.

## Quick Start

### One-Line Install

```bash
curl -fsSL https://raw.githubusercontent.com/ryan-rushton/ai-tooling/main/scripts/bootstrap.sh | bash
```

This will:

- Install global configuration files for all supported AI tools
- Copy the repository to `~/.ai-tooling`
- Set up tracking metadata for safe updates

### Install for a Specific Project

```bash
cd your-project
curl -fsSL https://raw.githubusercontent.com/ryan-rushton/ai-tooling/main/scripts/bootstrap.sh | bash -s -- --project-dir $(pwd)
```

## Supported Tools

| Tool                   | Global Config         | Project Config | File Format |
| ---------------------- | --------------------- | -------------- | ----------- |
| **Claude Code**        | `~/.claude/CLAUDE.md` | `CLAUDE.md`    | Markdown    |
| **Gemini Code Assist** | `~/.gemini/GEMINI.md` | `GEMINI.md`    | Markdown    |
| **Cursor**             | _(UI Settings)_       | `AGENTS.md`    | Markdown    |
| **OpenAI Codex**       | `~/.codex/AGENTS.md`  | `AGENTS.md`    | Markdown    |

**Note:** Cursor and Codex share the same `AGENTS.md` file in project directories.

## Configuration Files

### GLOBAL.md

Contains meta-behavioral preferences that apply across all projects:

- Communication style (succinct, direct)
- Code quality standards (comments explain "why" not "what")
- Problem-solving approach
- General development philosophy

Installed to global locations for Claude and Gemini.

### AGENTS.md

Contains repository-specific guidance:

- Testing strategies
- Build and lint commands
- Project architecture
- Code conventions
- Common tasks and workflows

Shared between Cursor and Codex. Installed to both global Codex location and project directories.

## Usage

### After Installation

1. **Review Global Files**: Customize your global preferences

   ```bash
   # Claude Code global config
   code ~/.claude/CLAUDE.md

   # Gemini Code Assist global config
   code ~/.gemini/GEMINI.md

   # Codex global config
   code ~/.codex/AGENTS.md
   ```

1. **Review Project Files**: Add project-specific instructions

   ```bash
   cd your-project

   # Claude Code project config
   code CLAUDE.md

   # Gemini Code Assist project config
   code GEMINI.md

   # Cursor + Codex shared config
   code AGENTS.md
   ```

1. **Customize**: Add your own sections below the managed sections marker

### Updating Configuration

The `ai-tooling` CLI provides convenient commands for managing your configurations:

```bash
# Update all configurations (global + local)
ai-tooling update

# Update only global configurations
ai-tooling update --global

# Update only local/project configurations
ai-tooling update --local

# Preview what would change without applying updates
ai-tooling update --dry-run

# Update the ai-tooling CLI itself to the latest version
ai-tooling self-update
```

The updater:

- ✅ Updates sections you haven't modified
- ⚠️ Skips sections you've customized
- 📊 Reports what was updated and what was skipped

### CLI Commands Reference

```bash
ai-tooling install                 # Install both global and local configs
ai-tooling install --global        # Install only global configs
ai-tooling install --local         # Install only local/project configs

ai-tooling update                  # Update all configurations
ai-tooling update --global         # Update only global configs
ai-tooling update --local          # Update only local configs
ai-tooling update --dry-run        # Preview changes

ai-tooling self-update             # Update the CLI itself

ai-tooling --version               # Show version
ai-tooling --help                  # Show help
```

## How It Works

### Section-Based Updates

Each configuration file is divided into sections (markdown headers). The installer:

1. Creates a `.ai-tooling-meta.json` file alongside each config
1. Stores SHA256 hashes of each section
1. On update, compares current hashes to originals
1. Updates only unmodified sections

Example metadata file:

```json
{
  "version": "1.0.0",
  "installed_at": "2026-01-17T10:30:00Z",
  "source_repo": "ai-tooling",
  "sections": {
    "Communication Style": "a1b2c3...",
    "Code Quality": "d4e5f6...",
    "Problem Solving": "g7h8i9..."
  }
}
```

### File Structure

```
~/.ai-tooling/
├── templates/
│   ├── GLOBAL.md          # Meta-behavior template
│   └── PROJECT.md         # Project-specific template
├── scripts/
│   ├── bootstrap.sh       # Curl entry point
│   ├── install.sh         # Main installer
│   └── update.sh          # Update script
├── config/
│   └── tool-mappings.json # Tool configuration
└── README.md
```

## Manual Installation

If you prefer not to use the bootstrap script:

```bash
# Clone the repository
git clone https://github.com/ryan-rushton/ai-tooling.git
cd ai-tooling

# Install globally only
./scripts/install.sh --global-only

# Install for current project only
./scripts/install.sh --project-only --project-dir /path/to/project

# Install both global and project configs
./scripts/install.sh --project-dir /path/to/project
```

## Customization

### Adding Custom Sections

Add your own sections below the managed sections marker in any config file:

```markdown
---

_This file is managed by ai-tooling. Customize sections below this line._

## My Custom Section

Your custom content here...
```

Custom sections won't be tracked or updated by the update script.

### Modifying Template Sections

If you modify a managed section (e.g., "Communication Style"), the update script will:

- Detect the change via hash comparison
- Skip updating that section
- Report it as "modified by user"

This allows you to override any default behavior while still receiving updates to other sections.

## Advanced Usage

### Multiple Projects

Install project configs for different repositories:

```bash
# Project A
cd ~/projects/project-a
~/.ai-tooling/scripts/install.sh --project-only --project-dir $(pwd)

# Project B
cd ~/projects/project-b
~/.ai-tooling/scripts/install.sh --project-only --project-dir $(pwd)
```

Each project gets independent tracking and can be updated separately.

### Version Control

**Global configs**: Typically not version controlled (personal preferences)

**Project configs**: Usually committed to git

```bash
# Add to version control
git add CLAUDE.md GEMINI.md AGENTS.md
git commit -m "Add AI tool configurations"
```

**Metadata files**: Should be gitignored

```bash
# Add to .gitignore
echo "*.ai-tooling-meta.json" >> .gitignore
```

## Troubleshooting

### "No metadata found" warning

This means a config file wasn't installed by this tool. Either:

- It was created manually (safe to ignore)
- The metadata was deleted (reinstall to track updates)

### Updates not applying

Ensure you're running from the install directory:

```bash
~/.ai-tooling/scripts/update.sh
```

### Conflicts after manual edits

The update script preserves your changes. If you want to reset a section:

1. Delete the section from your config file
1. Run the update script
1. The section will be restored from the template

## Contributing

Improvements to templates and scripts are welcome:

1. Fork the repository
1. Make your changes
1. Test with `--dry-run`
1. Submit a pull request

## License

MIT License - see LICENSE file for details

## References

- [Claude Code Documentation](https://code.claude.com/docs)
- [Gemini Code Assist](https://developers.google.com/gemini-code-assist)
- [Cursor Rules Documentation](https://cursor.com/docs/context/rules)
- [OpenAI Codex Agents.md Guide](https://developers.openai.com/codex/guides/agents-md)

______________________________________________________________________

**Sources:**

- [Rules | Cursor Docs](https://cursor.com/docs/context/rules)
- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Gemini CLI configuration](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/configuration.md)
- [OpenAI Codex Agents.md Guide](https://developers.openai.com/codex/guides/agents-md)
