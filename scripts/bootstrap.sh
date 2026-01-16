#!/usr/bin/env bash
set -euo pipefail

# AI Tooling Resources Bootstrap Script
# Usage: curl -fsSL https://raw.githubusercontent.com/ryan-rushton/ai-tooling-resources/main/scripts/bootstrap.sh | bash

REPO_URL="https://github.com/ryan-rushton/ai-tooling-resources.git"
TEMP_DIR=$(mktemp -d)
INSTALL_DIR="${AI_TOOLING_INSTALL_DIR:-$HOME/.ai-tooling-resources}"

echo "🤖 AI Tooling Resources Installer"
echo "=================================="
echo ""

# Check dependencies
command -v git >/dev/null 2>&1 || { echo "Error: git is required but not installed." >&2; exit 1; }

# Clone the repository
echo "📥 Cloning repository..."
git clone --depth 1 "$REPO_URL" "$TEMP_DIR" >/dev/null 2>&1

# Run the installer
echo ""
echo "🚀 Running installer..."
cd "$TEMP_DIR"
bash scripts/install.sh "$@"

# Clean up
cd - >/dev/null
rm -rf "$TEMP_DIR"

echo ""
echo "✅ Installation complete!"
echo ""
echo "Installed to: $INSTALL_DIR"
echo ""
echo "To update your configuration files later, run:"
echo "  $INSTALL_DIR/scripts/update.sh"
