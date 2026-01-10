
## Quick Reference Card

### Most Used (Learn These First)
```
hjkl        - Arrow keys (left/down/up/right)
w/b         - Word forward/back
0/^/$       - Line start/first-non-blank/end
gg/G        - File top/bottom
f{char}     - Find character on line
/{text}     - Search in file
n/N         - Next/previous match
*/#         - Search word under cursor forward/back
%           - Match bracket
Ctrl+o/i    - Jump back/forward

Exit Neovim:
:qa         - Quit all (exit Neovim completely)
:wqa        - Save all and quit
ZZ          - Save and quit (current file)
```

### Game Changers (Learn Week 2)
```
viw/vaw     - Select word (inner/around)
ciw/diw     - Change/delete word (cursor anywhere in word)
yiw         - Copy word
ci"/ci'     - Change inside quotes
di(/da(     - Delete inside/around parentheses
ci{/ca{     - Change inside/around braces
dap/vip     - Delete/select paragraph

Window Navigation:
Ctrl+w h/j/k/l - Move between windows (left/down/up/right)
:vsp/:sp    - Vertical/horizontal split
Ctrl+w q    - Close window
:only       - Close all but current window

LSP & Tools:
gd          - Go to definition (LSP)
K           - Hover docs (LSP)
<leader>ff  - Find files (Telescope)
<leader>fg  - Live grep (Telescope)
<leader>lv  - Open test in vsplit

Git Integration:
<leader>gp  - Preview hunk (show diff)
<leader>gs  - Stage hunk
]c / [c     - Next/previous hunk
<leader>gb  - Toggle git blame
<leader>gl  - Visual git log (Flog)
<leader>gf  - File history
:G          - Git status (interactive)

.           - Repeat last change
```

### Advanced Power Moves (Week 3+)
```
ma / `a     - Set mark / jump to mark
"ay / "ap   - Yank to register / paste from register
qa...q / @a - Record macro / execute macro
:s/old/new/g - Search and replace
Ctrl+v      - Visual block mode
g; / g,     - Jump to last/next change location
```

---

## Vim Philosophy

**The language of Vim:**
- **Operator** + **Motion** = Action
- Examples:
  - `d` (delete) + `w` (word) = `dw` (delete word)
  - `c` (change) + `i"` (inside quotes) = `ci"` (change inside quotes)
  - `y` (yank) + `ap` (around paragraph) = `yap` (copy paragraph)

**Operators:**
- `d` - delete
- `c` - change
- `y` - yank (copy)
- `v` - visual select
- `>` - indent
- `=` - auto-indent

**Motions:**
- `w`, `b`, `e` - word movements
- `f{char}`, `t{char}` - find character
- `i{`, `a"`, `ip` - text objects
- `$`, `^`, `0` - line positions
- `gg`, `G`, `{`, `}` - file positions

**The power:** Any operator works with any motion!
