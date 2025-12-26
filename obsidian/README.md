# Obsidian

Modular Obsidian configuration using GNU Stow. Apply different config sets to different vaults.

## Structure

```
obsidian/
├── base/       # Core settings (app.json, appearance.json, core-plugins.json, graph.json)
├── themes/     # Minimal theme
└── plugins/    # Community plugins (excalidraw)
```

## First Time Setup

If the vault already has `.obsidian/` files, stow will conflict. Remove or backup existing config first:

```bash
# For base (json files)
rm ~/Documents/Notes/.obsidian/{app.json,appearance.json,core-plugins.json,graph.json}

# For themes/plugins (entire directories)
rm -rf ~/Documents/Notes/.obsidian/{themes,plugins}
# Or backup: mv ~/Documents/Notes/.obsidian/themes{,.bak}

# Then stow
cd ~/.dotfiles/obsidian
stow -t ~/Documents/Notes base themes plugins
```

## Usage

```bash
cd ~/.dotfiles/obsidian

# Apply all configs to a vault
stow -t ~/Documents/Notes base themes plugins

# Apply only base + themes to another vault
stow -t ~/Projects/wiki base themes

# Remove config from a vault
stow -D -t ~/Documents/Notes base themes plugins
```

## Adding Plugin Sets

Split plugins into separate packages for modularity:

```bash
mkdir -p plugins-writing/.obsidian/plugins
mv plugins/.obsidian/plugins/some-writing-plugin plugins-writing/.obsidian/plugins/
```

Then apply selectively:
```bash
stow -t ~/Documents/Notes base themes plugins-writing
stow -t ~/Projects/code base plugins-dev
```

## Notes

- `workspace.json` is intentionally excluded (vault-specific state)
- Once stowed, `themes/` and `plugins/` are symlinked - themes/plugins installed via Obsidian UI automatically appear in dotfiles
- `base/` files are individual symlinks, changes in vault sync to dotfiles automatically
- To version a new theme/plugin: just `git add` it from dotfiles after installing in Obsidian