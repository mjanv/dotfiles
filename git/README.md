# Git

Git dotfiles with machine-specific user configuration separation.

### Create Local Configuration

The `.gitconfig` uses `[include]` to load machine-specific settings from `~/.gitconfig.local`.

Copy the example template:

```bash
cp ~/.dotfiles/git/.gitconfig.local.example ~/.gitconfig.local
```

Edit `~/.gitconfig.local` with your personal information:

```gitconfig
[user]
  name = Your Name
  email = your.email@example.com
```

**Important**: `~/.gitconfig.local` is NOT tracked in dotfiles for privacy/security.

