# Programs
alias j='just'
alias g='gedit'
alias c='code .'
alias n='nvim .'

# Claude Code
claudia() {
  source ~/.claude/.env && claude "$@"
}

alias cc='claudia'
alias cch='claudia --model haiku'
alias ccs='claudia --model sonnet'
alias cco='claudia --model opus'
alias ccy='claudia --dangerously-skip-permissions'
alias cchy='claudia --model haiku --dangerously-skip-permissions'
alias ccsy='claudia --model sonnet --dangerously-skip-permissions'
alias ccoy='claudia --model opus --dangerously-skip-permissions'

alias copilot-start='systemctl --user start copilot-api.service'
alias copilot-stop='systemctl --user stop copilot-api.service'
alias copilot-status='systemctl --user status copilot-api.service'
alias copilot-restart='systemctl --user restart copilot-api.service'

function tldr() {
	curl "cheat.sh/$1"
}

# Screenshoot
function scrd() {
	gnome-screenshot --area -f ~/Desktop/$1.png
}

function scrc() {
	gnome-screenshot --area --clipboard
}

# Python
alias p='python'
alias ip='ipython'
alias pt='pytest'

# Elixir
alias e='elixir'
alias ep='iex -S mix phx.server'
alias mf='mix format'
alias ms='mix phx.server'

# Docker
alias d='docker'
alias ds='docker stop $(docker ps -qa)'
alias dr='docker rm $(docker ps -qa)'
alias dc='docker-compose'
alias dcu='docker-compose up'
alias dcd='docker-compose down'
alias dcdv='docker-compose down --volumes'
