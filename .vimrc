
" Syntax check
syntax enable
" encoding
set encoding=UTF-8
set fileencoding=UTF-8
set termencoding=UTF-8
" under scroll
set scrolloff=2
" nmake .swap
set noswapfile
" nmake backup
set nowritebackup
set nobackup
" backspace Delete
set backspace=indent,eol,start

" silent heap
set vb t_vb=
set novisualbell
" use Clipboard OS
set clipboard=unnamed,autoselect
" show row and col
set ruler
" compatible off
set nocompatible
" highlight on
set showmatch
" highlight time
set matchtime=3
" show Invisible character
set listchars=tab:»-,trail:-,extends:»,precedes:«,nbsp:%,eol:↲
" incremental search
set incsearch
" show highlight word 
:set hlsearch
" Tab width
set tabstop=4
" shift width
set shiftwidth=4

" color mapping
set t_Co=256
set background=dark
colorscheme desert
let g:solarized_termcolors=256
set listchars=eol:¬,tab:▸\
" show rows
set number
" show title window
set title
set undolevels=300
" command search buffer
set history=10000
" IMEsetting
set iminsert=0
set imsearch=0
set imdisable
" status line
set laststatus=2
" message line width
set cmdheight=1
set ruler
" command bottom screen
set showcmd
" paste
set pastetoggle=<F12>
set clipboard=unnamed,unnamedplus,autoselect
" ESC response time
set timeoutlen=300
set mouse=a
" Command bottom
set showcmd
