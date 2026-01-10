# Neovim Learning Plan - Maxime

**Goal**: Master Neovim for Elixir development using my configured setup
**Start Date**: 2026-01-03
**Daily Practice**: 30 minutes minimum

---

## Current Configuration Overview

- **Leader Key**: `Space`
- **Plugin Manager**: lazy.nvim
- **LSP**: ElixirLS + NextLS configured
- **Main Tools**: Telescope, Neo-tree, LSP, Elixir-tools
- **Config Location**: `~/.dotfiles/nvim/.config/nvim/`

---

## Phase 1: Motion Fundamentals (Week 1)
> **Why**: Modal editing is what makes Neovim powerful. Must become muscle memory.

### Day 1-2: Basic Navigation
- [ ] Remove arrow keys from my workflow completely
- [ ] Practice `hjkl` for at least 20 minutes
- [ ] Learn `w` (word forward) and `b` (word backward)
- [ ] Master `0` (line start) and `$` (line end)
- [ ] Use `gg` (file top) and `G` (file bottom)

**Practice Exercise**: Navigate through `lib/` files in my Elixir project using only these keys

### Day 3-4: Text Objects (Game Changer!)
- [ ] `ciw` - Change inner word (cursor anywhere in word)
- [ ] `ci"` - Change inside double quotes
- [ ] `ci'` - Change inside single quotes
- [ ] `ca{` - Change around braces (includes the braces)
- [ ] `dap` - Delete around paragraph
- [ ] `dit` - Delete inside HTML/XML tag

**Elixir-Specific Practice**:
```elixir
# Try these on actual code:
# - ciw on variable names
# - ci" on strings in functions
# - ca{ on map literals
```

### Day 5-7: Search and Jump
- [ ] `f{char}` - Find character forward on line
- [ ] `F{char}` - Find character backward on line
- [ ] `t{char}` - Till character (stop before)
- [ ] `;` and `,` - Repeat f/F/t in same/opposite direction
- [ ] `/{pattern}` - Search forward in file
- [ ] `?{pattern}` - Search backward in file
- [ ] `n` / `N` - Next/previous search result
- [ ] `*` - Search for word under cursor
- [ ] `%` - Jump between matching brackets

**Practice**: Jump around Elixir function definitions, find `do`/`end` blocks

---

## Phase 2: Configured Tools Mastery (Week 2)
> **Why**: Leverage the powerful plugins already in my config

### Telescope (Primary Navigation Tool)
- [ ] `<leader>ff` - Find files (practice fuzzy matching: "usrcntrl" → user_controller.ex)
- [ ] `<leader>fg` - Live grep (search across all files)
- [ ] `<leader>fw` - Search current word under cursor
- [ ] `<leader>fd` - Search LSP diagnostics (errors/warnings)
- [ ] `<leader><space>` - Switch between open buffers
- [ ] `<leader>?` - Find recently opened files
- [ ] `<leader>/` - Fuzzy search in current buffer

**Daily Goal**: Navigate to 10 different files using only Telescope

### LSP Navigation (Code Intelligence)
- [ ] `K` - Hover documentation (read function docs)
- [ ] `gd` - Go to definition
- [ ] `<leader>ca` - Code actions (auto-imports, fixes)
- [ ] `Ctrl+o` - Jump back (built-in vim command)
- [ ] `Ctrl+i` - Jump forward

**Practice**: Read Elixir standard library docs via `K`, jump into dependencies

### Neo-tree (File Explorer)
- [ ] `Ctrl+n` - Toggle file tree
- [ ] `L` - Open file but keep focus on tree (custom mapping)
- [ ] Learn basic Neo-tree navigation (j/k, Enter, etc.)

**Note**: File tree shows dotfiles (hide_dotfiles = false in config)

### Elixir-Specific Tools
- [ ] `<space>fp` - From pipe (pipeline → nested calls)
- [ ] `<space>tp` - To pipe (nested calls → pipeline)
- [ ] `<space>em` - Expand macro (visual mode - select macro first)

**Practice File**: Find a complex pipeline in project, convert back/forth

### Test-Driven Development Navigation
- [ ] `<leader>ll` - Jump between implementation and test
- [ ] `<leader>lv` - Open related file in vertical split
- [ ] `<leader>lp` - Open related file in horizontal split

**Practice**: Work on a feature using TDD, jumping between `user.ex` ↔ `user_test.exs`

---

## Phase 3: Elixir Workflow Integration (Week 3)
> **Why**: Combine motions + tools into efficient workflow

### Daily Workflow Pattern
1. [ ] Open project: `nvim .` or `nvim lib/my_app/user.ex`
2. [ ] Find file with `<leader>ff`
3. [ ] Jump to definition with `gd`
4. [ ] Read docs with `K`
5. [ ] Edit with text objects (`ciw`, `ci"`, etc.)
6. [ ] Search project with `<leader>fg`
7. [ ] Jump to test with `<leader>ll`
8. [ ] Navigate back with `Ctrl+o`

### Common Elixir Patterns to Practice

**Pattern 1: Refactor function**
- [ ] `gd` to jump to function definition
- [ ] Use text objects to change parameters
- [ ] `<leader>fg` to find all usages
- [ ] Update each usage with `ciw`, `ci(`, etc.

**Pattern 2: Pipeline manipulation**
- [ ] Find pipeline with `<leader>fg some |> function`
- [ ] Use `<space>fp` to see nested version
- [ ] Edit the transformation
- [ ] `<space>tp` to convert back

**Pattern 3: Test-driven feature**
- [ ] Start in test file: `<leader>ff user_test`
- [ ] Write test
- [ ] `<leader>ll` to jump to implementation
- [ ] Write code
- [ ] `<leader>ll` back to verify test

### Buffer & Window Management
- [ ] `:split` or `:sp` - Horizontal split
- [ ] `:vsplit` or `:vsp` - Vertical split
- [ ] `Ctrl+w h/j/k/l` - Navigate between windows
- [ ] `Ctrl+w q` - Close window
- [ ] `:bd` - Close buffer
- [ ] `<leader><space>` - Quick buffer switch

---

## Phase 4: Advanced Techniques (Week 4+)
> **Why**: Become truly efficient

### Visual Mode
- [ ] `v` - Character-wise visual mode
- [ ] `V` - Line-wise visual mode
- [ ] `Ctrl+v` - Block visual mode
- [ ] `vip` - Select paragraph
- [ ] `vi{` - Select inside braces
- [ ] `gv` - Reselect last visual selection

**Elixir Use**: Select entire function with `vip`, select map with `vi{`

### Marks (Bookmarks)
- [ ] `m{a-z}` - Set mark (ma, mb, etc.)
- [ ] `` `{a-z} `` - Jump to exact position
- [ ] `'{a-z}` - Jump to line
- [ ] `:marks` - List all marks

**Use Case**: Mark important files/locations in large project

### Registers (Clipboard History)
- [ ] `"{a-z}y` - Yank to named register
- [ ] `"{a-z}p` - Paste from named register
- [ ] `"0p` - Paste last yank (not delete)
- [ ] `:reg` - View all registers

**Use Case**: Copy multiple snippets, paste in different order

### Macros (Record & Replay)
- [ ] `q{a-z}` - Start recording macro
- [ ] `q` - Stop recording
- [ ] `@{a-z}` - Execute macro
- [ ] `@@` - Repeat last macro
- [ ] `10@a` - Execute macro 10 times

**Elixir Example**: Record macro to convert function to pipe, apply to all similar functions

### Advanced Search & Replace
- [ ] `:%s/old/new/g` - Replace in whole file
- [ ] `:%s/old/new/gc` - Replace with confirmation
- [ ] `:'{mark1},'{mark2}s/old/new/g` - Replace in range
- [ ] Use `<leader>fg` then populate search with result

### Command-Line Mode
- [ ] `:!mix test` - Run external command
- [ ] `:r !date` - Insert command output
- [ ] `:term` - Open terminal in split
- [ ] `Ctrl+z` to background nvim, `fg` to return

---

## Weekly Goals

### Week 1 Checkpoint
- [ ] Navigate entire Elixir project without arrow keys
- [ ] Change function parameters using text objects
- [ ] Search and jump with f/F/t fluently

### Week 2 Checkpoint
- [ ] Find any file in <3 seconds using Telescope
- [ ] Jump to definitions and read docs reflexively
- [ ] Switch between test and implementation smoothly

### Week 3 Checkpoint
- [ ] Complete a feature using only Neovim (no VSCode fallback)
- [ ] Refactor a module using advanced motions
- [ ] Use pipe conversion tools naturally

### Week 4 Checkpoint
- [ ] Record and use at least one useful macro
- [ ] Use marks to navigate large refactoring
- [ ] Visual block mode for multi-cursor-like edits

---

## Key Cheatsheet (Quick Reference)

### My Custom Keybindings
```
Leader: Space

# Telescope
<leader>ff  - Find files
<leader>fg  - Live grep
<leader>fw  - Grep word under cursor
<leader>fd  - Search diagnostics
<leader><space> - Switch buffers

# LSP
K           - Hover docs
gd          - Go to definition
<leader>ca  - Code actions

# Elixir
<space>fp   - From pipe
<space>tp   - To pipe
<space>em   - Expand macro (visual)

# Test Navigation
<leader>ll  - Toggle test/implementation
<leader>lv  - Open related in vsplit
<leader>lp  - Open related in split

# File Explorer
Ctrl+n      - Toggle Neo-tree
```

### Essential Vim Motions
```
# Navigation
hjkl        - Left/Down/Up/Right
w/b         - Word forward/back
0/$         - Line start/end
gg/G        - File top/bottom

# Text Objects
ciw         - Change inner word
ci"/ci'     - Change inside quotes
ca{/ca(     - Change around braces/parens
dap         - Delete around paragraph

# Search
f{char}     - Find character forward
F{char}     - Find character backward
/{pattern}  - Search forward
n/N         - Next/previous result
*           - Search word under cursor
%           - Jump to matching bracket
```

---

## Progress Tracking

**Current Phase**: Phase 1 - Motion Fundamentals
**Days Practiced**: 0
**Comfort Level**: Beginner

### Daily Log
*Update after each practice session*

**2026-01-03**:
- Practice time:
- What I learned:
- Struggles:
- Wins:

---

## Resources

- **Config Files**: `~/.dotfiles/nvim/.config/nvim/`
- **Elixir Plugin Config**: `lua/plugins/elixir.lua`
- **LSP Config**: `lua/plugins/lsp-config.lua`
- **Telescope Config**: `lua/plugins/telescope.lua`
- **Test Navigation**: `lua/plugins/test-driven-development.lua`

## Notes & Discoveries

*Add your own insights, useful patterns, and "aha!" moments here*

---

## Next Actions

1. [ ] Open Elixir project with `nvim .`
2. [ ] Practice hjkl navigation for 10 minutes (NO arrow keys!)
3. [ ] Try `ciw` to change variable names
4. [ ] Use `<leader>ff` to find a file
5. [ ] Fill out first daily log entry above
