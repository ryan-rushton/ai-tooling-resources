#!/usr/bin/env bash
set -euo pipefail

# AI Tooling Resources Bootstrap Script
# Usage: curl -fsSL https://raw.githubusercontent.com/ryan-rushton/ai-tooling-resources/main/scripts/bootstrap.sh | bash

REPO_URL="https://github.com/ryan-rushton/ai-tooling-resources.git"
INSTALL_DIR="${AI_TOOLING_INSTALL_DIR:-$HOME/.ai-tooling-resources}"
BIN_DIR="$HOME/.local/bin"

echo "🤖 AI Tooling Resources Installer"
echo "=================================="
echo ""

# Check dependencies
command -v git >/dev/null 2>&1 || { echo "Error: git is required but not installed." >&2; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "Error: python3 is required but not installed." >&2; exit 1; }

# Check if uv is installed, install if not
if ! command -v uv >/dev/null 2>&1; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Clone the repository
echo "📥 Cloning repository to $INSTALL_DIR..."
if [ -d "$INSTALL_DIR" ]; then
    echo "   Removing existing installation..."
    rm -rf "$INSTALL_DIR"
fi

git clone --depth 1 "$REPO_URL" "$INSTALL_DIR" >/dev/null 2>&1

# Install the Python CLI
echo ""
echo "🐍 Installing ai-tooling CLI..."
cd "$INSTALL_DIR"
uv sync --quiet

# Create bin directory if it doesn't exist
mkdir -p "$BIN_DIR"

# Create a wrapper script that uses the venv
cat > "$BIN_DIR/ai-tooling" <<'EOF'
#!/usr/bin/env bash
INSTALL_DIR="${AI_TOOLING_INSTALL_DIR:-$HOME/.ai-tooling-resources}"
exec "$INSTALL_DIR/.venv/bin/python" -m ai_tooling.cli "$@"
EOF

chmod +x "$BIN_DIR/ai-tooling"

# Run initial installation
echo ""
echo "🚀 Running initial installation..."
"$BIN_DIR/ai-tooling" install "$@"

echo ""
echo "✅ Bootstrap complete!"
echo ""
echo "Installed to: $INSTALL_DIR"
echo "CLI available at: $BIN_DIR/ai-tooling"
echo ""

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "⚠️  Note: $BIN_DIR is not in your PATH."
    echo ""
    echo "Add this to your ~/.bashrc, ~/.zshrc, or ~/.profile:"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
fi

echo "To update your configuration files later, run:"
echo "  ai-tooling update"
echo ""
echo "For help, run:"
echo "  ai-tooling --help"
