# Neovim Navigation Commands Reference

## Character-Level Motion

| Key | Action | Details |
|-----|--------|---------|
| `h` | Move left | 1 character, stops at column 0 |
| `l` | Move right | 1 character, stops at line end |
| `j` | Move down | 1 line, maintains column |
| `k` | Move up | 1 line, maintains column |
| `5j` | Move down 5 | Prefix with count |

---

## Word Motion

| Key | Action | Details |
|-----|--------|---------|
| `w` | Word forward | Jumps to start of next word (punctuation = separate word) |
| `W` | WORD forward | Jumps to start of next WORD (whitespace-separated) |
| `b` | Word backward | Jumps to start of previous word |
| `B` | WORD backward | Jumps to start of previous WORD |
| `e` | End of word | Jumps to last character of current/next word |
| `ge` | End of word backward | Jumps to end of previous word |

**Word vs WORD:**
- word: `user_id` = 3 words (`user`, `_`, `id`)
- WORD: `user_id` = 1 WORD (whitespace-separated)

---

## Line Motion

| Key | Action | Details |
|-----|--------|---------|
| `0` | Hard line start | Column 0 (before indentation) |
| `^` | Soft line start | First non-blank character (after indentation) |
| `$` | Line end | Last character of line |
| `g_` | Last non-blank | Like `$` but ignores trailing whitespace |

**Tip:** In code, use `^` instead of `0` most of the time.

---

## File Motion

| Key | Action | Details |
|-----|--------|---------|
| `gg` | File top | Line 1, column 0 |
| `G` | File bottom | Last line, first non-blank |
| `50G` | Go to line 50 | Jump to specific line number |
| `50gg` | Go to line 50 | Alternative syntax |
| `:50` | Go to line 50 | Command mode alternative |

---

## Find Character (Current Line Only)

| Key | Action | Details |
|-----|--------|---------|
| `f{char}` | Find forward | Move onto next `{char}` on line |
| `F{char}` | Find backward | Move onto previous `{char}` on line |
| `t{char}` | Till forward | Move to position before next `{char}` |
| `T{char}` | Till backward | Move to position after previous `{char}` |
| `;` | Repeat find | Same direction as last f/F/t/T |
| `,` | Repeat find reverse | Opposite direction |

**Example:** `f(` then `;;` to jump through all `(` on line

---

## Search (Whole File)

| Key | Action | Details |
|-----|--------|---------|
| `/{pattern}` | Search forward | Supports regex |
| `?{pattern}` | Search backward | Supports regex |
| `n` | Next match | Same direction as last search |
| `N` | Previous match | Opposite direction |
| `*` | Search word forward | Whole word match under cursor |
| `#` | Search word backward | Whole word match under cursor |
| `g*` | Search partial forward | Partial match (finds `user` in `users`) |
| `g#` | Search partial backward | Partial match backward |

**Example:** Cursor on `user`, press `*` to find all exact matches

---

## Bracket/Pair Matching

| Key | Action | Details |
|-----|--------|---------|
| `%` | Jump to match | Works on `()`, `{}`, `[]`, `do/end` |

**Example:** On `(`, press `%` → jumps to matching `)`

---

## Paragraph Motion

| Key | Action | Details |
|-----|--------|---------|
| `{` | Previous paragraph | Previous blank line |
| `}` | Next paragraph | Next blank line |

**In code:** Use to jump between functions

---

## Screen Motion

| Key | Action | Details |
|-----|--------|---------|
| `H` | High | Top of visible screen |
| `M` | Middle | Middle of visible screen |
| `L` | Low | Bottom of visible screen |
| `Ctrl+d` | Down half-page | Scroll down half screen |
| `Ctrl+u` | Up half-page | Scroll up half screen |
| `Ctrl+f` | Forward full-page | Scroll down full screen |
| `Ctrl+b` | Backward full-page | Scroll up full screen |
| `zt` | Scroll to top | Current line to top of screen |
| `zz` | Scroll to center | Current line to center |
| `zb` | Scroll to bottom | Current line to bottom |

---

## Jump List Navigation

| Key | Action | Details |
|-----|--------|---------|
| `Ctrl+o` | Jump older | Go to previous position in jump list |
| `Ctrl+i` | Jump newer | Go forward in jump list |
| `:jumps` | View jump list | Show entire jump history |

**Example workflow:**
1. Press `gd` to jump to definition
2. Read the code
3. Press `Ctrl+o` to jump back

---

## Combining with Operators

All motions work with operators:

| Operator | Action | Example |
|----------|--------|---------|
| `d{motion}` | Delete | `dw` = delete word, `d$` = delete to end of line |
| `c{motion}` | Change | `ciw` = change inner word, `c}` = change to next paragraph |
| `y{motion}` | Yank (copy) | `yy` = yank line, `y$` = yank to end of line |
| `v{motion}` | Visual select | `vw` = select word, `v}` = select to next paragraph |

**Common patterns:**
- `dw` - Delete from cursor to start of next word
- `d$` - Delete from cursor to end of line (also `D`)
- `c^` - Change from cursor to start of line
- `yy` - Yank entire line (also `Y`)
- `dd` - Delete entire line
- `cc` - Change entire line (also `S`)

---

## Text Objects (Advanced)

Text objects are used **with operators** for powerful editing:

| Text Object | Action | Example |
|-------------|--------|---------|
| `iw` | Inner word | `ciw` = change word under cursor |
| `aw` | Around word | `daw` = delete word + surrounding space |
| `iW` | Inner WORD (whitespace-separated) | `ciW` = change WORD (e.g., `user.name` as one unit) |
| `aW` | Around WORD | `daW` = delete WORD + surrounding space |
| `i"` | Inside quotes | `ci"` = change text inside quotes |
| `a"` | Around quotes | `da"` = delete quotes and contents |
| `i'` | Inside single quotes | `ci'` = change text inside single quotes |
| `a'` | Around single quotes | `da'` = delete quotes and contents |
| `i(` or `i)` | Inside parens | `di(` = delete inside parentheses |
| `a(` or `a)` | Around parens | `da(` = delete parentheses and contents |
| `i{` or `i}` | Inside braces | `ci{` = change inside braces |
| `a{` or `a}` | Around braces | `da{` = delete braces and contents |
| `i[` or `i]` | Inside brackets | `di[` = delete inside brackets |
| `a[` or `a]` | Around brackets | `da[` = delete brackets and contents |
| `it` | Inside tag | `dit` = delete inside HTML/XML tag |
| `at` | Around tag | `dat` = delete tag and contents |
| `ip` | Inner paragraph | `vip` = select paragraph |
| `ap` | Around paragraph | `dap` = delete paragraph + blank line |

**Inner vs Around:**
- `i` = contents only
- `a` = contents + delimiters/whitespace

**Example:**
```elixir
def foo("hello", world)
        ^
```
- `ci"` → change `hello` (cursor anywhere in quotes)
- `ca"` → change `"hello"` including quotes
- `di(` → delete all function arguments
- `da(` → delete `(...)` including parentheses

---

## Visual Mode

| Key | Action | Details |
|-----|--------|---------|
| `v` | Character-wise visual | Select characters |
| `V` | Line-wise visual | Select entire lines |
| `Ctrl+v` | Block visual | Select rectangular blocks |
| `gv` | Reselect | Reselect last visual selection |
| `o` | Other end | Jump to other end of selection (in visual mode) |

**In visual mode, use any motion to extend selection:**
- `viw` - Select inner word
- `vi"` - Select inside quotes
- `vi{` - Select inside braces
- `vip` - Select paragraph
- `v$` - Select to end of line
- `vgg` - Select to top of file

### Selecting Words (Most Common Use Case)

| Command | Selects | Cursor Position | Use When |
|---------|---------|-----------------|----------|
| `viw` | Inner word only | Anywhere in word | Changing/copying just the word |
| `vaw` | Around word (includes space) | Anywhere in word | Deleting word and cleaning up spacing |
| `viW` | Inner WORD (whitespace-separated) | Anywhere in WORD | Selecting compound terms like `user.name` |
| `vaW` | Around WORD (includes space) | Anywhere in WORD | Deleting compound terms cleanly |

**Key insight:** Cursor can be **anywhere** in the word - beginning, middle, or end.

**Word vs WORD:**
- **word** (`w`): Separated by punctuation. `user_name` = 1 word, `user.name` = 3 words (`user`, `.`, `name`)
- **WORD** (`W`): Separated by whitespace only. `user.name.first` = 1 WORD

**Examples:**

```elixir
def create_user(params) do
       ^cursor anywhere here
```
- `viw` → selects `create_user`
- `vaw` → selects `create_user` + trailing space

```elixir
user.first_name
     ^cursor here
```
- `viw` → selects `first_name` (stops at dot)
- `viW` → selects `user.first_name` (entire thing)

```elixir
foo bar baz
    ^cursor on bar
```
- `viw` then `d` → deletes `bar`, leaves: `foo  baz` (double space)
- `vaw` then `d` → deletes `bar` and space, leaves: `foo baz` (clean)

**Without visual mode (faster once comfortable):**
- `ciw` - Change inner word (no visual step)
- `diw` - Delete inner word
- `yiw` - Yank (copy) inner word
- `daw` - Delete around word (cleaner deletion)

---

## Marks (Bookmarks)

| Key | Action | Details |
|-----|--------|---------|
| `m{a-z}` | Set mark | `ma` sets mark 'a' at cursor position |
| `` `{a-z} `` | Jump to mark | `` `a `` jumps to exact position of mark 'a' |
| `'{a-z}` | Jump to mark line | `'a` jumps to first non-blank of mark 'a' line |
| `:marks` | List marks | Show all marks |
| `:delmarks {a-z}` | Delete marks | `:delmarks a` deletes mark 'a' |

**Special marks (automatic):**
- `` `. `` - Jump to last change
- `` `^ `` - Jump to last insert position
- `` `` `` - Jump to position before last jump

---

## Registers (Clipboard)

| Key | Action | Details |
|-----|--------|---------|
| `"{a-z}y` | Yank to register | `"ayiw` yanks word to register 'a' |
| `"{a-z}p` | Paste from register | `"ap` pastes from register 'a' |
| `"0p` | Paste last yank | Register 0 always has last yank (not delete) |
| `:reg` | View registers | Show all register contents |
| `"+y` | Yank to system clipboard | Requires clipboard support |
| `"+p` | Paste from system clipboard | Requires clipboard support |

**Special registers:**
- `"0` - Last yank
- `"1-"9` - Delete history (1 is most recent)
- `""` - Unnamed register (default)
- `"+` - System clipboard
- `"*` - Selection clipboard (X11)

---

## Macros (Record & Replay)

| Key | Action | Details |
|-----|--------|---------|
| `q{a-z}` | Start recording | `qa` starts recording to register 'a' |
| `q` | Stop recording | Stop current macro recording |
| `@{a-z}` | Execute macro | `@a` executes macro in register 'a' |
| `@@` | Repeat last macro | Repeat the most recently executed macro |
| `10@a` | Execute 10 times | Execute macro 'a' 10 times |

**Example workflow:**
1. `qa` - Start recording to register 'a'
2. Perform edits (e.g., `^i// <Esc>j` to comment a line)
3. `q` - Stop recording
4. `@a` - Execute macro once
5. `10@a` - Execute 10 more times

---

## Search & Replace

| Command | Action | Details |
|---------|--------|---------|
| `:s/old/new/` | Replace first | Replace first occurrence on current line |
| `:s/old/new/g` | Replace all | Replace all occurrences on current line |
| `:%s/old/new/g` | Replace in file | Replace all occurrences in file |
| `:%s/old/new/gc` | Replace with confirm | Ask for confirmation each time |
| `:'<,'>s/old/new/g` | Replace in selection | Visual mode range |
| `:10,20s/old/new/g` | Replace in range | Lines 10-20 |

**Example:**
```vim
:%s/user_id/userId/gc
```
→ Replace all `user_id` with `userId`, asking for confirmation each time

---

## Window Management

| Key | Action | Details |
|-----|--------|---------|
| `:split` or `:sp` | Horizontal split | Split window horizontally |
| `:vsplit` or `:vsp` | Vertical split | Split window vertically |
| `Ctrl+w h` | Move left | Move to window on left |
| `Ctrl+w j` | Move down | Move to window below |
| `Ctrl+w k` | Move up | Move to window above |
| `Ctrl+w l` | Move right | Move to window on right |
| `Ctrl+w w` | Cycle windows | Move to next window |
| `Ctrl+w q` | Close window | Close current window |
| `Ctrl+w =` | Equal size | Make all windows equal size |
| `Ctrl+w _` | Maximize height | Maximize current window height |
| `Ctrl+w |` | Maximize width | Maximize current window width |

---

## Buffer Management

| Command | Action | Details |
|---------|--------|---------|
| `:ls` or `:buffers` | List buffers | Show all open buffers |
| `:b {number}` | Switch to buffer | `:b 2` switches to buffer 2 |
| `:b {name}` | Switch by name | `:b user` switches to buffer matching 'user' |
| `:bn` | Next buffer | Switch to next buffer |
| `:bp` | Previous buffer | Switch to previous buffer |
| `:bd` | Delete buffer | Close current buffer |
| `:bd {number}` | Delete specific | `:bd 2` closes buffer 2 |
| `:%bd` | Delete all buffers | Close all buffers |

---

## Window Management

### Understanding the Three-Layer System

Neovim has three distinct concepts:

1. **Buffers** = Files in memory
   - A buffer is a file loaded into memory
   - Can have many buffers open but only see a few at once
   - Buffers exist even when not visible
   - Check with `:ls` or `<leader><space>`

2. **Windows** = Views/Panes
   - A window is a viewport displaying a buffer
   - Split screen to see multiple windows
   - Each window shows one buffer
   - This is what you navigate between

3. **Tabs** = Window Layouts
   - A tab is a collection of windows
   - Like workspaces or different screen arrangements
   - Less commonly used than buffers + windows

**Mental model:**
- **Buffers** = Open documents
- **Windows** = Split screen panes viewing documents
- **Tabs** = Different screen arrangements

### Creating Window Splits

| Command | Action | Details |
|---------|--------|---------|
| `:split` or `:sp` | Horizontal split | Split window (one above other) |
| `:vsplit` or `:vsp` | Vertical split | Split window (side by side) |
| `Ctrl+w s` | Horizontal split | Same as `:sp` |
| `Ctrl+w v` | Vertical split | Same as `:vsp` |
| `:vsp {file}` | Open file in vsplit | Open specific file in new vertical split |
| `:sp {file}` | Open file in split | Open specific file in new horizontal split |
| `<leader>lv` | Test in vsplit | Open related test in vsplit (custom) |
| `<leader>lp` | Test in split | Open related test in split (custom) |

**Example:**
```
Original:                After :vsplit:
┌─────────────┐         ┌──────┬──────┐
│  user.ex    │         │user  │user  │
└─────────────┘         └──────┴──────┘
```

### Navigating Between Windows

**Core navigation: `Ctrl+w` + direction**

| Key | Action | Details |
|-----|--------|---------|
| `Ctrl+w h` | Move left | Move to window on the left |
| `Ctrl+w j` | Move down | Move to window below |
| `Ctrl+w k` | Move up | Move to window above |
| `Ctrl+w l` | Move right | Move to window on the right |
| `Ctrl+w w` | Cycle windows | Move to next window |
| `Ctrl+w p` | Previous window | Go to previously focused window |

**Mnemonic:** Same `hjkl` navigation, prefix with `Ctrl+w`

**Example layout:**
```
┌────────────┬──────────┐
│  window 1  │ window 2 │  ← Ctrl+w l to move right
├────────────┴──────────┤    Ctrl+w h to move left
│   window 3            │  ← Ctrl+w k to move up
└───────────────────────┘    Ctrl+w j to move down
```

### Closing Windows

| Command | Action | Details |
|---------|--------|---------|
| `Ctrl+w q` | Quit window | Close current window |
| `Ctrl+w c` | Close window | Same as `Ctrl+w q` |
| `:q` | Quit window | Close current window |
| `:only` | Close all others | Keep only current window |
| `Ctrl+w o` | Only this window | Same as `:only` |

**Important:** Closing a window doesn't close the buffer (file stays in memory).

### Resizing Windows

| Command | Action | Details |
|---------|--------|---------|
| `Ctrl+w =` | Equal size | Make all windows equal size |
| `Ctrl+w _` | Maximize height | Maximize current window height |
| `Ctrl+w \|` | Maximize width | Maximize current window width |
| `Ctrl+w +` | Increase height | Make window taller |
| `Ctrl+w -` | Decrease height | Make window shorter |
| `Ctrl+w >` | Increase width | Make window wider |
| `Ctrl+w <` | Decrease width | Make window narrower |
| `10 Ctrl+w +` | Increase by 10 | Increase height by 10 lines |
| `5 Ctrl+w >` | Increase by 5 | Increase width by 5 columns |

### Moving Windows Around

| Command | Action | Details |
|---------|--------|---------|
| `Ctrl+w r` | Rotate windows | Rotate windows downward/rightward |
| `Ctrl+w R` | Rotate reverse | Rotate windows upward/leftward |
| `Ctrl+w x` | Exchange | Exchange current with next window |
| `Ctrl+w H` | Move to far left | Move window to far left (full height) |
| `Ctrl+w J` | Move to bottom | Move window to bottom (full width) |
| `Ctrl+w K` | Move to top | Move window to top (full width) |
| `Ctrl+w L` | Move to far right | Move window to far right (full height) |

### Working with Neo-tree (File Tree)

Neo-tree opens in a separate window (usually on the left).

**My custom keybindings:**
- `Ctrl+n` → Toggle Neo-tree on/off (neotree.lua:36)
- `L` → Open file but keep focus on tree (neotree.lua:14, in Neo-tree only)

**Workflow:**
```
┌──────┬──────────┐
│ Neo- │  editor  │
│ tree │  (code)  │
└──────┴──────────┘
```

1. `Ctrl+n` → open Neo-tree
2. Navigate with `j/k` to select file
3. Press `L` → opens file in editor, focus stays in tree
4. Or press `Enter` → opens file and moves focus to editor
5. `Ctrl+w l` → manually move to editor
6. `Ctrl+w h` → move back to Neo-tree
7. `Ctrl+n` → close Neo-tree when done

### Practical Workflows

#### Workflow 1: Side-by-Side Editing (Implementation + Test)

```bash
nvim lib/my_app/user.ex
```

Then:
1. `<leader>lv` → opens test in vertical split
   ```
   ┌─────────────┬──────────────┐
   │  user.ex    │ user_test.exs│
   └─────────────┴──────────────┘
   ```
2. `Ctrl+w l` → move to test
3. `Ctrl+w h` → move back to implementation
4. Edit in both, switching as needed

#### Workflow 2: File Tree + Editor

1. `Ctrl+n` → open Neo-tree
2. Browse files with `j/k`
3. Press `L` on files → opens in editor, stay in tree
4. `Ctrl+w l` → move to editor when ready
5. `Ctrl+n` → close Neo-tree when done

#### Workflow 3: Three-Way Split

1. `nvim user.ex`
2. `:vsp user_controller.ex` → vertical split
3. `Ctrl+w w` → move to controller window
4. `:sp user_view.ex` → horizontal split in right pane

Result:
```
┌──────────┬──────────┐
│          │controller│
│ user.ex  ├──────────┤
│          │   view   │
└──────────┴──────────┘
```

Navigate: `Ctrl+w h/j/k/l` to move between windows

#### Workflow 4: Same File, Different Locations

Useful for comparing different parts of a long file:

1. `:sp` → split horizontally (same file in both)
2. Navigate to different parts in each window
3. Edit in one, see changes reflected in the other

### Common Window Scenarios

| Scenario | Solution |
|----------|----------|
| "Neo-tree is open, how do I edit?" | `Ctrl+w l` (move right) |
| "Too many splits, I'm confused" | `:only` (close all but current) |
| "Want test and implementation together" | `<leader>lv` (auto-opens test in vsplit) |
| "How do I close Neo-tree?" | `Ctrl+n` (toggle) or `Ctrl+w q` in tree |
| "Want same file in two windows" | `:sp` (shows same file in both panes) |

### Window Quick Reference

**Navigation (most important):**
```
Ctrl+w h/j/k/l  - Move between windows (left/down/up/right)
Ctrl+w w        - Cycle to next window
```

**Creating:**
```
:vsp            - Vertical split (side by side)
:sp             - Horizontal split (top/bottom)
<leader>lv      - Open test in vsplit (custom)
```

**Managing:**
```
Ctrl+w q        - Close current window
Ctrl+w =        - Make all windows equal size
:only           - Close all windows except current
```

**With Neo-tree:**
```
Ctrl+n          - Toggle file tree
L               - Open file, stay in tree (custom, in Neo-tree only)
Ctrl+w l        - Move from tree to editor
Ctrl+w h        - Move from editor to tree
```

---

## Tab Management

Tabs are **less important** in Neovim than in other editors. Buffers + windows are usually sufficient.

| Command | Action | Details |
|---------|--------|---------|
| `:tabnew` | New tab | Open new empty tab |
| `:tabnew {file}` | New tab with file | Open file in new tab |
| `gt` | Next tab | Switch to next tab |
| `gT` | Previous tab | Switch to previous tab |
| `{n}gt` | Go to tab n | `2gt` goes to tab 2 |
| `:tabclose` | Close tab | Close current tab |
| `:tabonly` | Close other tabs | Keep only current tab |

**When to use tabs:**
- Separate workspaces (e.g., one tab for feature, another for bug fix)
- Different projects or contexts
- Most of the time, buffers + windows are enough

---

## Undo/Redo

| Key | Action | Details |
|-----|--------|---------|
| `u` | Undo | Undo last change |
| `Ctrl+r` | Redo | Redo last undone change |
| `U` | Undo line | Undo all changes on current line |
| `:earlier 5m` | Time travel back | Undo to state 5 minutes ago |
| `:later 5m` | Time travel forward | Redo to state 5 minutes later |

---

## Exiting Neovim

### Quit Commands

| Command | What It Does | When to Use |
|---------|-------------|-------------|
| `:q` | Quit current window | Single window, no changes |
| `:q!` | Quit without saving | Discard changes in current window |
| `:qa` | **Quit all** (exit Neovim) | Close everything and exit |
| `:qa!` | Quit all without saving | Force exit, discard all changes |
| `:wq` | Write and quit | Save current file and close window |
| `:wqa` | Write all and quit all | Save all changes and exit |
| `:xa` | Exit all | Save modified files and exit (same as `:wqa`) |

### Quick Exit Shortcuts

**In normal mode** (no `:` needed):

| Key | What It Does | Equivalent To |
|-----|-------------|---------------|
| `ZZ` | Save and quit | `:wq` |
| `ZQ` | Quit without saving | `:q!` |

**Important:** `ZZ` and `ZQ` only work for the current window. For multiple windows, use `:qa` or `:wqa`.

### Common Scenarios

| Scenario | Command | Why |
|----------|---------|-----|
| Single file, want to save and exit | `ZZ` or `:wq` | Fastest way out |
| Single file, discard changes | `ZQ` or `:q!` | Don't save |
| Multiple windows open, exit everything | `:qa` | Closes all windows and exits |
| Multiple windows, save all and exit | `:wqa` | Saves everything then exits |
| `:q` says "X more files to edit" | `:qa` | You have multiple buffers open |
| Unsure if you have unsaved changes | `:qa` | Will prompt if there are unsaved changes |
| Force exit no matter what | `:qa!` | Nuclear option - discards everything |

### Why `:q` Doesn't Always Exit

When you have multiple windows or buffers:

```
┌──────┬──────┐
│ win1 │ win2 │  ← Two windows open
└──────┴──────┘
```

- `:q` → Closes **one window**, Neovim stays open
- `:qa` → Exits **Neovim completely** ✓

**Rule of thumb:**
- Use `:q` when working with single file
- Use `:qa` to exit Neovim completely

### Save and Exit in One Command

**Best practice:**
```vim
:wqa
```

This saves all modified files and exits Neovim. Safe and clean.

**Alternative:**
```vim
:xa
```

Same as `:wqa` - saves modified files and exits.

---

## Editing Commands

| Key | Action | Details |
|-----|--------|---------|
| `i` | Insert before cursor | Enter insert mode |
| `I` | Insert at line start | Enter insert at first non-blank |
| `a` | Append after cursor | Enter insert mode after cursor |
| `A` | Append at line end | Enter insert at end of line |
| `o` | Open line below | Create new line below and insert |
| `O` | Open line above | Create new line above and insert |
| `r{char}` | Replace character | Replace single character under cursor |
| `R` | Replace mode | Enter replace mode (overwrites) |
| `x` | Delete character | Delete character under cursor |
| `X` | Delete backward | Delete character before cursor |
| `s` | Substitute character | Delete character and enter insert |
| `S` | Substitute line | Delete line and enter insert (same as `cc`) |
| `~` | Toggle case | Toggle case of character under cursor |
| `J` | Join lines | Join current line with next |
| `gJ` | Join without space | Join lines without inserting space |

---

## Copy/Paste

| Key | Action | Details |
|-----|--------|---------|
| `yy` or `Y` | Yank line | Copy entire line |
| `y{motion}` | Yank motion | `yw` yanks word, `y$` yanks to end of line |
| `p` | Paste after | Paste after cursor/line |
| `P` | Paste before | Paste before cursor/line |
| `]p` | Paste and adjust indent | Paste and match indentation |

---

## Indentation

| Key | Action | Details |
|-----|--------|---------|
| `>>` | Indent line | Indent current line right |
| `<<` | Unindent line | Indent current line left |
| `>{motion}` | Indent motion | `>}` indents paragraph |
| `<{motion}` | Unindent motion | `<}` unindents paragraph |
| `=` | Auto-indent | `=}` auto-indents paragraph |
| `gg=G` | Auto-indent file | Auto-indent entire file |

**In visual mode:**
- `>` - Indent selection
- `<` - Unindent selection
- `=` - Auto-indent selection

---

## Repeat & Dot Command

| Key | Action | Details |
|-----|--------|---------|
| `.` | Repeat last change | Most powerful command in Vim |
| `;` | Repeat last f/F/t/T | Repeat character search |
| `,` | Reverse f/F/t/T | Reverse character search |
| `n` | Repeat last search | Next match |
| `&` | Repeat last :s | Repeat last substitution |

**Example:**
1. `ciw` then type `newName` → changes word to `newName`
2. Move to another word
3. `.` → repeats the change (replaces word with `newName`)

---

## Custom Keybindings (My Config)

### Telescope (File Navigation)
| Key | Action | Location |
|-----|--------|----------|
| `<leader>ff` | Find files | telescope.lua:18 |
| `<leader>fg` | Live grep (search in files) | telescope.lua:21 |
| `<leader>fw` | Grep word under cursor | telescope.lua:20 |
| `<leader>fd` | Search diagnostics | telescope.lua:22 |
| `<leader><space>` | Switch buffers | telescope.lua:10 |
| `<leader>?` | Recently opened files | telescope.lua:9 |
| `<leader>/` | Fuzzy search current buffer | telescope.lua:11 |
| `<leader>fh` | Search help tags | telescope.lua:19 |

### LSP (Language Server)
| Key | Action | Location |
|-----|--------|----------|
| `K` | Hover documentation | lsp-config.lua:24 |
| `gd` | Go to definition | lsp-config.lua:25 |
| `<leader>ca` | Code actions | lsp-config.lua:26 |

### Elixir-Specific
| Key | Action | Location |
|-----|--------|----------|
| `<space>fp` | From pipe (pipeline → nested) | elixir.lua:18 |
| `<space>tp` | To pipe (nested → pipeline) | elixir.lua:19 |
| `<space>em` | Expand macro (visual mode) | elixir.lua:20 |

### Test Navigation
| Key | Action | Location |
|-----|--------|----------|
| `<leader>ll` | Toggle test/implementation | test-driven-development.lua:44 |
| `<leader>lv` | Open related in vsplit | test-driven-development.lua:47 |
| `<leader>lp` | Open related in split | test-driven-development.lua:46 |
| `<leader>ltn` | Open related in new tab | test-driven-development.lua:45 |
| `<leader>lc` | Clear alternate files | test-driven-development.lua:48 |

### File Explorer
| Key | Action | Location |
|-----|--------|----------|
| `Ctrl+n` | Toggle Neo-tree | neotree.lua:36 |
| `L` | Open without losing focus | neotree.lua:14 (in Neo-tree) |

### Git Integration
| Key | Action | Location |
|-----|--------|----------|
| `<leader>gp` | Preview hunk (show diff popup) | git.lua:11 |
| `<leader>gs` | Stage hunk | git.lua:12 |
| `<leader>gr` | Reset hunk (discard changes) | git.lua:13 |
| `<leader>gu` | Undo stage hunk | git.lua:14 |
| `<leader>gb` | Toggle git blame inline | git.lua:17 |
| `]c` | Next hunk (next change) | git.lua:20 |
| `[c` | Previous hunk (previous change) | git.lua:21 |
| `<leader>gl` | Visual git log (Flog) | git.lua:31 |
| `<leader>gf` | File history (Flog) | git.lua:32 |

---

## Git Integration (Detailed)

You have three powerful git plugins configured:
1. **Gitsigns** - Visual git status in editor
2. **Fugitive** - Full git integration
3. **Flog** - Visual git log browser

### Gitsigns - Visual Git Status

**What you see:**

Gitsigns shows git diff markers in the left gutter (sign column):
- `+` green = added lines
- `~` yellow = modified lines
- `-` red = deleted lines

**Your keybindings:**

| Key | Action | What It Does |
|-----|--------|--------------|
| `<leader>gp` | Preview hunk | Show diff popup for current change |
| `<leader>gs` | Stage hunk | Stage just this change (not whole file) |
| `<leader>gr` | Reset hunk | Discard this change |
| `<leader>gu` | Undo stage | Unstage this change |
| `<leader>gb` | Toggle blame | Show who/when changed current line |
| `]c` | Next hunk | Jump to next change in file |
| `[c` | Previous hunk | Jump to previous change in file |

**What's a hunk?** A continuous section of changed lines. You can stage/reset individual hunks instead of entire files.

**Example workflow - Selective staging:**
1. Edit multiple parts of a file
2. `]c` → jump to first change
3. `<leader>gp` → preview it
4. `<leader>gs` → stage it (or skip)
5. `]c` → next change
6. Repeat
7. `:G` → see what's staged
8. Commit

**Inline blame:**
- `<leader>gb` → shows commit info at end of current line
- Shows: author, date, commit message
- `<leader>gb` again → toggle off

### Fugitive - Full Git Integration

**Main command:** `:Git` or `:G`

**Common commands:**

| Command | What It Does |
|---------|-------------|
| `:Git` or `:G` | Interactive git status |
| `:Git add %` | Stage current file (% = current file) |
| `:Git commit` | Commit |
| `:Git commit -m "msg"` | Commit with message |
| `:Git push` | Push to remote |
| `:Git pull` | Pull from remote |
| `:Git diff` | Show diff |
| `:Gdiffsplit` | Side-by-side diff |
| `:Git blame` | Show git blame |
| `:Git log` | Show commit history |
| `:Git log %` | History for current file |
| `:Git log -p` | History with diffs (shows actual changes) |
| `:Git log -p %` | File history with diffs |
| `:Git show <hash>` | Show specific commit |

**Interactive Git Status (`:G`):**

Opens a git status window showing:
- Modified files (red M)
- Staged files (green A/M)
- Untracked files (red ?)

**In the status window:**
- `j/k` → navigate files
- `-` → stage/unstage file under cursor
- `=` → toggle inline diff
- `cc` → commit (opens commit message editor)
- `Enter` → open file
- `g?` → help (shows all commands)

**Side-by-side diff:**

`:Gdiffsplit` opens split windows:
```
┌──────────┬──────────┐
│  HEAD    │ Working  │
│ (git)    │ (your    │
│ version  │ changes) │
└──────────┴──────────┘
```

Navigate between windows with `Ctrl+w h/l`.

**Git blame:**

`:Git blame` opens blame window showing:
- Commit hash
- Author
- Date
- For each line

Press `Enter` on a line to see the full commit.

### Flog - Visual Git Log

**Your keybindings:**

| Key | Action | What It Does |
|-----|--------|--------------|
| `<leader>gl` | Visual git log | Open Flog (full repo history) |
| `<leader>gf` | File history | Open file-specific history |

**What Flog shows:**

A visual commit graph with branches and merges:
```
* abc1234 (HEAD -> main) Fix user validation
* def5678 Add email field
| * ghi9012 (feature/new-ui) Update styles
|/
* jkl3456 Initial commit
```

**Navigation in Flog:**

| Key | Action |
|-----|--------|
| `j/k` | Move up/down commits |
| `Enter` | Open commit details (shows diff) |
| `q` | Close Flog |
| `a` | Toggle showing all branches |
| `gb` | Open commit in git blame |
| `dd` | Open diff for commit |
| `u` | Update Flog view |

**Flog commands:**

| Command | What It Shows |
|---------|--------------|
| `:Flog` | Full history, current branch |
| `:Flog -all` | All branches |
| `:Flog -path=%` | Current file only |
| `:Flogsplit` | Open in split |
| `:Flogsplit -path=%` | File history in split |
| `:Flog -search="pattern"` | Search commit messages |
| `:Flog -patch-search="pattern"` | Search diffs (code changes) |
| `:Flog -author="name"` | Filter by author |
| `:Flog -since="1 week ago"` | Filter by date |

**Combining filters:**
```vim
:Flog -path=% -author="John" -since="1 month ago"
```

Shows commits to current file, by John, in the last month.

### Common Git Workflows

#### Workflow 1: Quick Commit

```vim
:G                        " Open git status
" Navigate to files with j/k
" Press - to stage files
cc                        " Commit (opens editor)
" Type commit message
:wq                       " Save and close
:Git push                 " Push to remote
```

#### Workflow 2: Review Changes Before Commit

```vim
:G                        " Git status
" Navigate to file
=                         " Toggle inline diff
" Review changes
-                         " Stage if good
cc                        " Commit
```

#### Workflow 3: Selective Staging (Hunks)

```vim
" Make changes to file
]c                        " Jump to first change
<leader>gp                " Preview it
<leader>gs                " Stage this hunk
]c                        " Next change
<leader>gp                " Preview
<leader>gs                " Stage
:G                        " Check what's staged
cc                        " Commit
```

#### Workflow 4: Find When Bug Was Introduced

```vim
<leader>ff                " Find file with bug
<leader>gl                " Open visual git log
" or
<leader>gf                " File-specific history
" Navigate with j/k
Enter                     " See commit diff
" Find the commit that introduced bug
<leader>gb                " See blame info
```

#### Workflow 5: Compare Versions

```vim
:Gdiffsplit               " See current changes
" or
:Git diff HEAD~5          " Compare with 5 commits ago
" or
:Git diff main            " Compare with main branch
```

#### Workflow 6: View File History

```vim
:e lib/user.ex            " Open file
<leader>gf                " Visual file history (Flog)
" or
:Git log -p %             " Text-based with diffs
```

#### Workflow 7: See What Changed Recently

```vim
:Git log -p -5            " Last 5 commits with diffs
" or
:Git log -p --since="yesterday"
```

#### Workflow 8: Understand a Line's History

```vim
" Place cursor on line
<leader>gb                " Toggle blame
" See: author, date, commit message
:Git show <hash>          " See full commit (copy hash from blame)
```

### Git Quick Reference

**Gitsigns (in editor):**
```
<leader>gp  - Preview hunk
<leader>gs  - Stage hunk
<leader>gr  - Reset hunk
<leader>gb  - Toggle blame
]c / [c     - Next/previous hunk
```

**Fugitive (git commands):**
```
:G          - Git status (interactive)
:Git add %  - Stage current file
:Git commit - Commit
:Git push   - Push
:Gdiffsplit - Side-by-side diff
:Git blame  - Git blame
```

**Flog (visual history):**
```
<leader>gl  - Visual git log (full repo)
<leader>gf  - File history
Enter       - Show commit diff (in Flog)
a           - Toggle all branches (in Flog)
q           - Close Flog
```

**In git status window (`:G`):**
```
-           - Stage/unstage file
=           - Toggle diff
cc          - Commit
Enter       - Open file
```

### Tips

**Tip 1: Gutter markers update in real-time**
- As you edit, gitsigns updates the `+`/`~`/`-` markers
- Use `]c`/`[c` to jump between your changes

**Tip 2: Stage parts of files, not all**
- Use `<leader>gs` to stage individual hunks
- Allows for cleaner, focused commits

**Tip 3: Blame shows inline**
- `<leader>gb` shows commit info at end of line
- No separate window needed

**Tip 4: Flog is faster for browsing**
- Use `<leader>gl` to visually browse history
- Press `Enter` on commits to see what changed
- Much faster than reading `git log` output

**Tip 5: Combine tools**
- Use Telescope to find code (`<leader>fg`)
- Use Flog to see when it was added (`<leader>gf`)
- Use blame to see who wrote it (`<leader>gb`)
- Use Fugitive to see full commit (`:Git show <hash>`)

**Tip 6: Diff before commit**
- `:Gdiffsplit` before committing
- Review changes side-by-side
- Catch mistakes before they're committed

