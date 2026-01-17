#!/usr/bin/env bash
set -euo pipefail

# AI Tooling Installer
# Installs global and project-specific AI tool configuration files

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$REPO_ROOT/config/tool-mappings.json"
INSTALL_DIR="${AI_TOOLING_INSTALL_DIR:-$HOME/.ai-tooling}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}$1${NC}"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Parse command line arguments
INSTALL_TYPE="both"  # both, global, project
PROJECT_DIR=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --global-only)
            INSTALL_TYPE="global"
            shift
            ;;
        --project-only)
            INSTALL_TYPE="project"
            shift
            ;;
        --project-dir)
            PROJECT_DIR="$2"
            shift 2
            ;;
        *)
            print_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# If no project dir specified and installing project files, use current directory
if [[ "$INSTALL_TYPE" == "project" ]] || [[ "$INSTALL_TYPE" == "both" ]]; then
    if [[ -z "$PROJECT_DIR" ]]; then
        PROJECT_DIR="$(pwd)"
    fi
fi

# Function to compute SHA256 hash of file sections
compute_section_hash() {
    local file="$1"
    local section="$2"

    # Extract section content and hash it
    awk -v section="$section" '
        /^# / { current_section = $0; in_section = 0 }
        /^## / {
            if (current_section == section || $0 == section) {
                in_section = 1
            } else {
                in_section = 0
            }
            next
        }
        in_section { print }
    ' "$file" | shasum -a 256 | cut -d' ' -f1
}

# Function to create metadata file
create_metadata() {
    local target_file="$1"
    local metadata_file="${target_file}.ai-tooling-meta.json"

    if [[ ! -f "$target_file" ]]; then
        return
    fi

    local sections=$(grep '^## ' "$target_file" | sed 's/^## //')
    local json_sections=""

    while IFS= read -r section; do
        if [[ -n "$section" ]]; then
            local hash=$(compute_section_hash "$target_file" "## $section")
            json_sections="$json_sections\"$section\": \"$hash\","
        fi
    done <<< "$sections"

    # Remove trailing comma
    json_sections="${json_sections%,}"

    cat > "$metadata_file" <<EOF
{
  "version": "1.0.0",
  "installed_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "source_repo": "ai-tooling",
  "sections": {
    $json_sections
  }
}
EOF
}

# Function to expand tilde in paths
expand_path() {
    local path="$1"
    echo "${path/#\~/$HOME}"
}

# Function to install a file
install_file() {
    local template="$1"
    local target="$2"
    local create_meta="${3:-true}"

    target=$(expand_path "$target")
    local target_dir=$(dirname "$target")

    # Create directory if it doesn't exist
    mkdir -p "$target_dir"

    # Copy file
    cp "$REPO_ROOT/templates/$template" "$target"
    print_success "Installed: $target"

    # Create metadata
    if [[ "$create_meta" == "true" ]]; then
        create_metadata "$target"
    fi
}

# Copy repository to install directory
print_header "Installing AI Tooling to $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"
cp -r "$REPO_ROOT"/* "$INSTALL_DIR/"
print_success "Repository installed to $INSTALL_DIR"

echo ""

# Install global files
if [[ "$INSTALL_TYPE" == "global" ]] || [[ "$INSTALL_TYPE" == "both" ]]; then
    print_header "Installing global configuration files..."

    # Claude Code
    install_file "GLOBAL.md" "~/.claude/CLAUDE.md"

    # Gemini Code Assist
    install_file "GLOBAL.md" "~/.gemini/GEMINI.md"

    # Codex
    install_file "AGENTS.md" "~/.codex/AGENTS.md"

    echo ""
fi

# Install project files
if [[ "$INSTALL_TYPE" == "project" ]] || [[ "$INSTALL_TYPE" == "both" ]]; then
    if [[ -n "$PROJECT_DIR" ]]; then
        print_header "Installing project configuration files to $PROJECT_DIR..."

        # Install CLAUDE.md
        install_file "GLOBAL.md" "$PROJECT_DIR/CLAUDE.md"

        # Install GEMINI.md
        install_file "GLOBAL.md" "$PROJECT_DIR/GEMINI.md"

        # Install AGENTS.md (shared by Cursor and Codex)
        install_file "AGENTS.md" "$PROJECT_DIR/AGENTS.md"

        echo ""
    fi
fi

print_header "Installation Summary"
echo ""
echo "Global files installed:"
echo "  - Claude Code:  ~/.claude/CLAUDE.md"
echo "  - Gemini:       ~/.gemini/GEMINI.md"
echo "  - Codex:        ~/.codex/AGENTS.md"
echo ""

if [[ -n "$PROJECT_DIR" ]]; then
    echo "Project files installed to $PROJECT_DIR:"
    echo "  - CLAUDE.md   (Claude Code)"
    echo "  - GEMINI.md   (Gemini Code Assist)"
    echo "  - AGENTS.md   (Cursor + Codex)"
    echo ""
fi

print_success "Installation complete!"
echo ""
echo "Next steps:"
echo "  1. Review and customize the installed configuration files"
echo "  2. Run 'ai-tooling-update' to check for updates later"
echo ""
echo "To update configuration files, run:"
echo "  $INSTALL_DIR/scripts/update.sh"
