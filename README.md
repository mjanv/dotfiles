# Dotfiles

> Maxime Janvier personal dotfiles configuration

## Packages

### Terminals

- [Bash](bash/)
- [Zsh](zsh/)
- [Git](git/)

### Text editors

- [Vim](vim/)
- [Neovim](nvim/)
- [VS Code](code/)
- [Obsidian](obsidian/README.md)

### AI assistants

- [Claude Code](claude/)


## Installation

```bash
sudo apt install stow
./stow.sh all     # Install all packages (bash, zsh, git, vim, nvim, code, claude)
./stow.sh bash    # Install specific package(s)
```

**Obsidian** requires manual stowing with vault-specific target directories. See [obsidian/README.md](obsidian/README.md) for details.

To install Firacode font and Nerd icons, install the font from [Nerd Fonts](https://www.nerdfonts.com/font-downloads)

## Resources

- [GNU Stow manual](https://www.gnu.org/software/stow/manual/stow.html)
- [Manage Your Dotfiles Like a Superhero - Jake Wiesler](https://www.jakewiesler.com/blog/managing-dotfiles)
