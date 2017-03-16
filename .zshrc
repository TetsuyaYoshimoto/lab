
export LANG=ja_JP.UTF-8
#export PATH=$PATH:/usr/include/c++/4.8/
export PATH=/usr/local/bin:/usr/bin:$PATH

autoload -U compinit promptinit
compinit
promptinit

prompt walters

setopt auto_param_slash
setopt mark_dirs
setopt list_types
setopt auto_menu
setopt auto_param_keys
setopt interactive_comments
setopt magic_equal_subst
setopt complete_in_word
setopt always_last_prompt

bindkey "^[[Z" reverse-menu-complete

setopt print_eight_bit
setopt extended_glob
setopt globdots
setopt list_packed

zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'
zstyle ':completion:*:default' menu select=2
zstyle ':completion:*' ignore-parents parent pwd ..
zstyle ':completion:*:sudo:*' command-path /usr/local/sbin /usr/local/bin /usr/sbin /usr/bin /sbin /bin

autoload -Uz select-word-style
select-word-style default
zstyle ':zle:*' word-chars " /=;@:{},|"
zstyle ':zle:*' word-style unspecified

HISTFILE=~/.zsh_history
HISTSIZE=1000000
SAVEHIST=1000000

setopt pushd_ignore_dups
setopt share_history
setopt hist_ignore_all_dups
setopt hist_ignore_space
setopt hist_reduce_blanks

autoload -U colors ; colors
local DEFAULT=%{$reset_color%}
local RED=%{$fg[red]%}
local GREEN=%{$fg[green]%}
local YELLOW=%{$fg[yellow]%}
local BLUE=%{$fg[blue]%}
local PURPLE=%{$fg[purple]%}
local CYAN=%{$fg[cyan]%}
local WHITE=%{$fg[white]%}

PROMPT='[%F{cyan}%B%n%b%f]%# '
RPROMPT='[%F{green}%B%~%b%f]'

export LSCOLORS=exfxcxdxbxegedabagacad
export LS_COLORS='di=36:ln=35:so=32:pi=33:ex=32:bd=46;34:cd=43;34:su=41;30:sg=46;30:tw=42;30:ow=43;30'

zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}

alias ...="../.."
alias ....="../../.."

# グローバルエイリアス
alias -g L='| less'
alias -g G="| grep"
