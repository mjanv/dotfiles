# Programs
alias j='just'
alias g='gedit'
alias c='code .'
alias n='nvim'

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

# Docker
alias d='docker'
alias ds='docker stop $(docker ps -qa)'
alias dr='docker rm $(docker ps -qa)'
alias dc='docker-compose'
alias dcu='docker-compose up'
alias dcd='docker-compose down'
alias dcdv='docker-compose down --volumes'
