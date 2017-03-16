
# 環境変数
export LANG=ja_JP.UTF-8
#export PATH=$PATH:/usr/include/c++/4.8/
export PATH=/usr/local/bin:/usr/bin:$PATH

# This will set the default prompt to the walters theme
prompt walters
# '#' 以降をコメントとして扱う
setopt interactive_comments
# 日本語ファイル名を表示可能にする
setopt print_eight_bit
setopt extended_glob
setopt globdots
setopt list_packed
# 単語の区切り文字を指定する
autoload -Uz select-word-style
select-word-style default
# 以下で指定した文字は単語区切りとみなされる
zstyle ':zle:*' word-chars " /=;@:{},|"
zstyle ':zle:*' word-style unspecified


# ヒストリを保存するファイル
HISTFILE=~/.zsh_history
# メモリに保存されるヒストリの件数
HISTSIZE=1000000
# 保存されるヒストリの件数
SAVEHIST=1000000
# 重複したディレクトリを追加しない
setopt pushd_ignore_dups
# 同時に起動したzsh間においてヒストリを共有する
setopt share_history
# 同じコマンドをヒストリに残さない
setopt hist_ignore_all_dups
# スペースから始まるコマンド行はヒストリに残さない
setopt hist_ignore_space
# ヒストリに保存するときに余分なスペースを削除する
setopt hist_reduce_blanks

# 色の設定(プロンプトに色付けをおこなう)
autoload -U colors ; colors
local DEFAULT=%{$reset_color%}
local RED=%{$fg[red]%}
local GREEN=%{$fg[green]%}
local YELLOW=%{$fg[yellow]%}
local BLUE=%{$fg[blue]%}
local PURPLE=%{$fg[purple]%}
local CYAN=%{$fg[cyan]%}
local WHITE=%{$fg[white]%}

# lsコマンドでの色付け
export LSCOLORS=exfxcxdxbxegedabagacad
export LS_COLORS='di=36:ln=35:so=32:pi=33:ex=32:bd=46;34:cd=43;34:su=41;30:sg=46;30:tw=42;30:ow=43;30'

# beepを無効化
setopt no_beep
# フローコントロールを無効化
setopt no_flow_control
# ディレクトリ名のみでもcdする
setopt auto_cd
# cdしたら自動的にpushdする
setopt auto_pushd

#エイリアス
alias ...="../.."
alias ....="../../.."
