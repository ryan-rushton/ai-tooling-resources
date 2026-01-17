#!/usr/bin/env bash
set -euo pipefail

# AI Tooling Update Script
# Updates configuration files while preserving user modifications

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
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

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# Parse command line arguments
DRY_RUN=false
PROJECT_DIR=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --project-dir)
            PROJECT_DIR="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Function to expand tilde in paths
expand_path() {
    local path="$1"
    echo "${path/#\~/$HOME}"
}

# Function to compute SHA256 hash of file sections
compute_section_hash() {
    local file="$1"
    local section="$2"

    # Extract section content and hash it
    awk -v section="$section" '
        /^## / {
            if ($0 == section) {
                in_section = 1
                next
            } else {
                in_section = 0
            }
        }
        /^#[^#]/ { in_section = 0 }
        in_section { print }
    ' "$file" | shasum -a 256 | cut -d' ' -f1
}

# Function to extract section from file
extract_section() {
    local file="$1"
    local section="$2"

    awk -v section="$section" '
        /^## / {
            if ($0 == section) {
                in_section = 1
                print
                next
            } else if (in_section) {
                exit
            }
        }
        /^#[^#]/ && in_section { exit }
        in_section { print }
    ' "$file"
}

# Function to replace section in file
replace_section() {
    local file="$1"
    local section="$2"
    local new_content="$3"
    local temp_file=$(mktemp)

    awk -v section="$section" -v new_content="$new_content" '
        /^## / {
            if ($0 == section) {
                in_section = 1
                print new_content
                next
            } else if (in_section) {
                in_section = 0
            }
        }
        /^#[^#]/ && in_section { in_section = 0 }
        !in_section { print }
    ' "$file" > "$temp_file"

    mv "$temp_file" "$file"
}

# Function to update a file
update_file() {
    local target="$1"
    local template="$2"

    target=$(expand_path "$target")
    local metadata_file="${target}.ai-tooling-meta.json"

    # Check if target file exists
    if [[ ! -f "$target" ]]; then
        print_warning "Target file not found: $target (skipping)"
        return
    fi

    # Check if metadata exists
    if [[ ! -f "$metadata_file" ]]; then
        print_warning "No metadata found for $target (skipping - was it installed manually?)"
        return
    fi

    print_info "Checking $target..."

    local template_file="$REPO_ROOT/templates/$template"
    local sections=$(grep '^## ' "$template_file" | sed 's/^## //')
    local updated_sections=0
    local skipped_sections=0
    local skipped_list=""

    while IFS= read -r section; do
        if [[ -z "$section" ]]; then
            continue
        fi

        # Get original hash from metadata
        local original_hash=$(jq -r ".sections[\"$section\"] // empty" "$metadata_file")

        if [[ -z "$original_hash" ]]; then
            # New section in template
            print_info "  New section found: $section"
            continue
        fi

        # Compute current hash
        local current_hash=$(compute_section_hash "$target" "## $section")

        if [[ "$current_hash" == "$original_hash" ]]; then
            # Section unchanged, update it
            if [[ "$DRY_RUN" == false ]]; then
                local new_section=$(extract_section "$template_file" "## $section")
                replace_section "$target" "## $section" "$new_section"

                # Update metadata hash
                local new_hash=$(compute_section_hash "$target" "## $section")
                local temp_meta=$(mktemp)
                jq ".sections[\"$section\"] = \"$new_hash\"" "$metadata_file" > "$temp_meta"
                mv "$temp_meta" "$metadata_file"

                updated_sections=$((updated_sections + 1))
            else
                print_success "  Would update: $section"
                updated_sections=$((updated_sections + 1))
            fi
        else
            # Section modified by user, skip it
            skipped_sections=$((skipped_sections + 1))
            skipped_list="$skipped_list\n    - $section"
        fi
    done <<< "$sections"

    if [[ $updated_sections -gt 0 ]]; then
        if [[ "$DRY_RUN" == false ]]; then
            print_success "Updated $updated_sections section(s) in $target"
        else
            print_info "Would update $updated_sections section(s) in $target"
        fi
    fi

    if [[ $skipped_sections -gt 0 ]]; then
        print_warning "Skipped $skipped_sections modified section(s):$(echo -e "$skipped_list")"
    fi

    echo ""
}

# Update repository
print_header "Updating AI Tooling..."
cd "$INSTALL_DIR"
git pull --quiet origin main 2>/dev/null || print_warning "Could not update repository (not a git repo or no internet)"
echo ""

if [[ "$DRY_RUN" == true ]]; then
    print_info "DRY RUN MODE - No files will be modified"
    echo ""
fi

# Update global files
print_header "Checking global configuration files..."
update_file "~/.claude/CLAUDE.md" "GLOBAL.md"
update_file "~/.gemini/GEMINI.md" "GLOBAL.md"
update_file "~/.codex/AGENTS.md" "AGENTS.md"

# Update project files if specified
if [[ -n "$PROJECT_DIR" ]]; then
    print_header "Checking project configuration files in $PROJECT_DIR..."
    update_file "$PROJECT_DIR/CLAUDE.md" "GLOBAL.md"
    update_file "$PROJECT_DIR/GEMINI.md" "GLOBAL.md"
    update_file "$PROJECT_DIR/AGENTS.md" "AGENTS.md"
fi

print_header "Update Complete!"

if [[ "$DRY_RUN" == true ]]; then
    echo ""
    print_info "This was a dry run. Run without --dry-run to apply updates."
fi
