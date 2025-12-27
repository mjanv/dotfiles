# Neovim

Modern Neovim configuration focused on LSP, completions, and Elixir development.

## Features

- **Plugin Manager**: [lazy.nvim](https://github.com/folke/lazy.nvim) with lazy loading
- **LSP**: Mason + nvim-lspconfig with auto-install
- **Completion**: nvim-cmp + LuaSnip with snippet support
- **Syntax**: Treesitter with auto-install and highlight
- **File Navigation**: Telescope fuzzy finder + Neo-tree file explorer
- **Git Integration**: Fugitive + Gitsigns
- **Terminal**: ToggleTerm with multiple layouts
- **AI Assistance**: Supermaven
- **Elixir Support**: Dedicated LSP and tooling
- **TDD Workflow**: Quick navigation between source and test files

## Themes

- **Active**: Catppuccin (priority 1000)
- **Available**: Shades of Purple (priority 1100, disabled)

## Core Settings

```lua
expandtab = true        # Use spaces instead of tabs
tabstop = 2             # 2 spaces per tab
softtabstop = 2         # Backspace deletes 2 spaces
shiftwidth = 2          # Indent by 2 spaces
mapleader = " "         # Space as leader key
```

## Plugins by Category

### LSP & Completions

#### Mason (`williamboman/mason.nvim`)
LSP server installer with auto-install support.

#### nvim-lspconfig (`neovim/nvim-lspconfig`)
LSP configuration for Lua.

**Keymaps**:

| Key | Action |
|-----|--------|
| `K` | Hover documentation |
| `gd` | Go to definition |
| `<leader>ca` | Code actions |

#### nvim-cmp (`hrsh7th/nvim-cmp`)
Autocompletion with snippet support.

**Keymaps**:

| Key | Action |
|-----|--------|
| `<C-b>` | Scroll docs up |
| `<C-f>` | Scroll docs down |
| `<C-Space>` | Trigger completion |
| `<C-e>` | Abort completion |
| `<CR>` | Confirm selection |

**Sources**: LuaSnip, buffer

### File Navigation

#### Telescope (`nvim-telescope/telescope.nvim`)
Fuzzy finder for files, buffers, grep, and more.

**Keymaps**:

| Key | Action |
|-----|--------|
| `<leader>?` | Recently opened files |
| `<leader><space>` | Find buffers |
| `<leader>/` | Fuzzy search current buffer |
| `<leader>ff` | Find files |
| `<leader>fh` | Search help tags |
| `<leader>fw` | Search current word |
| `<leader>fg` | Live grep |
| `<leader>fd` | Search diagnostics |

#### Neo-tree (`nvim-neo-tree/neo-tree.nvim`)
File explorer with git integration.

**Keymaps**:

| Key | Action |
|-----|--------|
| `<C-n>` | Toggle Neo-tree |
| `L` | Open file without losing focus |

**Config**: Shows hidden files, hides only `.git`

### Syntax & Highlighting

#### Treesitter (`nvim-treesitter/nvim-treesitter`)
Syntax highlighting and code understanding.

**Features**: Auto-install parsers, syntax highlighting, smart indentation

### Git

#### Fugitive (`tpope/vim-fugitive`)
Git wrapper for Vim commands.

#### Gitsigns (`lewis6991/gitsigns.nvim`)
Git decorations and inline blame.

**Keymaps**:

| Key | Action |
|-----|--------|
| `<leader>gp` | Preview hunk |

### Terminal

#### ToggleTerm (`akinsho/toggleterm.nvim`)
Terminal integration with multiple layouts.

**Keymaps**:

| Key | Action |
|-----|--------|
| `<leader>th` | Horizontal terminal |
| `<leader>tv` | Vertical terminal |
| `<leader>tt` | Terminal in new tab |
| `<leader>tf` | Floating terminal |
| `<leader>tg` | Toggle all terminals |

**Terminal mode keymaps**:

| Key | Action |
|-----|--------|
| `<esc>` or `jk` | Exit terminal mode |
| `<C-h/j/k/l>` | Navigate windows |

### Formatting

#### none-ls (`nvimtools/none-ls.nvim`)
Formatting and diagnostics.

**Formatters**: stylua (Lua), spell completion

**Keymaps**:

| Key | Action |
|-----|--------|
| `<leader>gf` | Format buffer |

### AI & Completion

#### Supermaven (`supermaven-inc/supermaven-nvim`)
AI-powered code completion.

#### Which-key (`folke/which-key.nvim`)
Shows keybinding hints (300ms timeout).

### Language-Specific

#### Elixir Tools (`elixir-tools/elixir-tools.nvim`)
Elixir LSP with NextLS and ElixirLS.

**Keymaps**:

| Key | Action | Mode |
|-----|--------|------|
| `<space>fp` | Convert from pipe | Normal |
| `<space>tp` | Convert to pipe | Normal |
| `<space>em` | Expand macro | Visual |

**Features**: Projectionist integration, test lenses disabled, dialyzer disabled

### Test-Driven Development

#### other.nvim (`rgroli/other.nvim`)
Navigate between related files (source ↔ test, LiveView ↔ template).

**Keymaps**:

| Key | Action |
|-----|--------|
| `<leader>ll` | Show related files |
| `<leader>ltn` | Open in new tab |
| `<leader>lp` | Open in horizontal split |
| `<leader>lv` | Open in vertical split |
| `<leader>lc` | Clear cache |

**Supported patterns**:
- Livewire, Angular, Laravel, Rails, Golang, Python, React, Rust
- Elixir: `lib/**/*.ex` ↔ `test/**/*_test.exs`
- Phoenix LiveView: `*_live.ex` ↔ `*_live.html.heex`

### UI

#### Lualine (`nvim-lualine/lualine.nvim`)
Status line with Dracula theme.

#### Bufferline (`akinsho/bufferline.nvim`)
Buffer/tab line with icons.

#### Nerdicons (`glepnir/nerdicons.nvim`)
Icon picker (`:NerdIcons`).

## Installation

```bash
# Stow the configuration
cd ~/.dotfiles
stow nvim

# Launch Neovim - lazy.nvim will auto-install on first run
nvim

# Install LSP servers via Mason
:Mason
```

## Structure

```
nvim/.config/nvim/
├── init.lua                          # Entry point, lazy.nvim bootstrap
├── lazy-lock.json                    # Plugin version lockfile
└── lua/
    ├── vim-options.lua               # Core Vim settings
    ├── plugins.lua                   # Nerdicons plugin
    └── plugins/
        ├── completions.lua           # nvim-cmp + LuaSnip + which-key
        ├── copilot.lua               # Supermaven AI
        ├── elixir.lua                # Elixir LSP and tools
        ├── git.lua                   # Fugitive + Gitsigns
        ├── lsp-config.lua            # Mason + LSP config
        ├── lualine.lua               # Lualine + Bufferline
        ├── neotree.lua               # File explorer
        ├── none-ls.lua               # Formatting (stylua)
        ├── telescope.lua             # Fuzzy finder
        ├── terminal.lua              # ToggleTerm
        ├── test-driven-development.lua  # other.nvim
        ├── themes.lua                # Catppuccin + Shades of Purple
        └── treesitter.lua            # Syntax highlighting
```

## Special Features

### Terminal Background Sync
Auto-syncs terminal background color with Neovim colorscheme (init.lua:19-29).

### Lazy Loading
Most plugins load on-demand for faster startup time.

## Dependencies

- Neovim >= 0.9
- Git
- [ripgrep](https://github.com/BurntSushi/ripgrep) (for Telescope live_grep)
- [fd](https://github.com/sharkdp/fd) (optional, for faster file finding)
- Node.js (for some LSP servers)
- Nerd Font (for icons)

## Resources

- [From 0 to IDE in NEOVIM from scratch | FREE COURSE // EP 1 - typecraft](https://www.youtube.com/watch?v=zHTeCSVAFNY)
- [Yet Another Neovim Setup Guide — 2024 Edition](https://www.vineeth.io/posts/neovim-setup)