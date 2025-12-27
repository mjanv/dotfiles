#!/bin/bash

# Dotfiles installation script
#
# Usage:
#   ./stow.sh            # Stow all packages
#   ./stow.sh all        # Stow all packages
#   ./stow.sh bash git   # Stow specific packages
#
# Note: obsidian is stowed separately with custom target directories
#       See obsidian/README.md for details

set -e

DOTFILES_DIR="$HOME/.dotfiles"
ALL_PACKAGES=(bash zsh git vim nvim code claude)

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if stow is installed
if ! command -v stow &> /dev/null; then
    echo -e "${RED}Error: GNU Stow is not installed${NC}"
    echo -e "${YELLOW}Install it with: sudo apt install stow${NC}"
    exit 1
fi

echo -e "${GREEN}✓${NC} GNU Stow found"

# Check if we're in the dotfiles directory
if [ ! -d "$DOTFILES_DIR" ]; then
    echo -e "${RED}Error: Dotfiles directory not found at $DOTFILES_DIR${NC}"
    exit 1
fi

echo -e "${GREEN}✓${NC} Dotfiles directory found\n"

# Determine which packages to stow
if [ $# -eq 0 ] || [ "$1" = "all" ]; then
    PACKAGES=("${ALL_PACKAGES[@]}")
    echo -e "${BLUE}Stowing all packages...${NC}\n"
else
    PACKAGES=("$@")
    echo -e "${BLUE}Stowing packages: ${PACKAGES[*]}${NC}\n"
fi

# Stow each package
cd "$DOTFILES_DIR"
for package in "${PACKAGES[@]}"; do
    if [ -d "$package" ]; then
        echo -e "  ${YELLOW}→${NC} Stowing $package..."
        stow -R "$package" 2>&1 | grep -v "BUG in find_stowed_path" || true
        echo -e "  ${GREEN}✓${NC} $package stowed successfully"
    else
        echo -e "  ${YELLOW}⚠${NC} Package $package not found, skipping"
    fi
done

echo -e "${GREEN}Installation complete!${NC}"
echo -e "${YELLOW}Note:${NC} Some configurations may require a shell restart to take effect"
