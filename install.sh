#!/bin/bash

echo "=== Password Manager CLI Installer ==="
echo ""

# Detect current directory
INSTALL_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "📁 Install directory: $INSTALL_DIR"

# Detect shell
if [ -n "$FISH_VERSION" ] || command -v fish &> /dev/null; then
    SHELL_TYPE="fish"
    CONFIG_FILE="$HOME/.config/fish/config.fish"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_TYPE="bash"
    CONFIG_FILE="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_TYPE="zsh"
    CONFIG_FILE="$HOME/.zshrc"
else
    echo "❌ Shell tidak terdeteksi. Silakan setup manual."
    exit 1
fi

echo "🐚 Detected shell: $SHELL_TYPE"
echo "📝 Config file: $CONFIG_FILE"
echo ""

# Create config file if not exists
mkdir -p "$(dirname "$CONFIG_FILE")"
touch "$CONFIG_FILE"

# Check if alias already exists
if grep -q "alias pm=" "$CONFIG_FILE" 2>/dev/null; then
    echo "⚠️  Alias 'pm' sudah ada. Menghapus yang lama..."
    if [ "$SHELL_TYPE" = "fish" ]; then
        sed -i '/alias pm=/d' "$CONFIG_FILE"
        sed -i '/alias pmcli=/d' "$CONFIG_FILE"
    else
        sed -i '/alias pm=/d' "$CONFIG_FILE"
        sed -i '/alias pmcli=/d' "$CONFIG_FILE"
    fi
fi

# Add aliases
echo "" >> "$CONFIG_FILE"
echo "# Password Manager CLI" >> "$CONFIG_FILE"
if [ "$SHELL_TYPE" = "fish" ]; then
    echo "alias pm='python3 $INSTALL_DIR/pm_interactive.py'" >> "$CONFIG_FILE"
    echo "alias pmcli='python3 $INSTALL_DIR/pm.py'" >> "$CONFIG_FILE"
else
    echo "alias pm='python3 $INSTALL_DIR/pm_interactive.py'" >> "$CONFIG_FILE"
    echo "alias pmcli='python3 $INSTALL_DIR/pm.py'" >> "$CONFIG_FILE"
fi

echo ""
echo "✅ Instalasi berhasil!"
echo ""
echo "Cara menggunakan:"
echo "  1. Reload shell config:"
if [ "$SHELL_TYPE" = "fish" ]; then
    echo "     source ~/.config/fish/config.fish"
elif [ "$SHELL_TYPE" = "bash" ]; then
    echo "     source ~/.bashrc"
else
    echo "     source ~/.zshrc"
fi
echo ""
echo "  2. Atau tutup dan buka terminal baru"
echo ""
echo "  3. Jalankan password manager:"
echo "     pm              # Mode interaktif"
echo "     pmcli list      # Mode CLI"
echo ""
echo "🎉 Selamat menggunakan!"
