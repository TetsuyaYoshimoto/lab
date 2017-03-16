
# egv
export LANG=ja_JP.UTF-8
#export PATH=$PATH:/usr/include/c++/4.8/
export PATH=/usr/local/bin:/usr/bin:$PATH

# this will set the default prompt to the walters theme
prompt walters
# '#' use comment
setopt interactive_comments
# show jp file
setopt print_eight_bit
setopt extended_glob
setopt globdots
setopt list_packed
# word break
zstyle ':zle:*' word-chars " /=;@:{},|"
zstyle ':zle:*' word-style unspecified

# history file
HISTFILE=~/.zsh_history
# memory history
HISTSIZE=50
# save history
SAVEHIST=50
# history sharing
setopt share_history
# not overlap command
setopt hist_ignore_all_dups
setopt hist_reduce_blanks

# color mapping
autoload -U colors ; colors
local DEFAULT=%{$reset_color%}
local RED=%{$fg[red]%}
local GREEN=%{$fg[green]%}
local YELLOW=%{$fg[yellow]%}
local BLUE=%{$fg[blue]%}
local PURPLE=%{$fg[purple]%}
local CYAN=%{$fg[cyan]%}
local WHITE=%{$fg[white]%}

export LSCOLORS=exfxcxdxbxegedabagacad
export LS_COLORS='di=36:ln=35:so=32:pi=33:ex=32:bd=46;34:cd=43;34:su=41;30:sg=46;30:tw=42;30:ow=43;30'

# no beep
setopt no_beep
# no control
setopt no_flow_control
# auto cd
setopt auto_cd

#alias
alias ...="../.."
alias ....="../../.."
