# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

from time import localtime, strftime

# Reassign to avoid lsp(ruff_lsp) errors
config = config  # noqa: F821
c = c  # noqa: F821

config.load_autoconfig()

# User agent
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "*",
)

# Variables
leader = " "
ss_dir = "~/Pictures/Screenshots/"
timestamp = strftime("%Y-%m-%d-%H-%M-%S", localtime())  # updates on every config-source
terminal = "alacritty"
editor = "nvim"
username = "2kabhishek"
homepage = "https://2kabhishek.github.io/links"

# General
c.editor.command = [terminal, "-e", editor, "{}"]
c.auto_save.session = True
c.zoom.default = "75%"
# c.window.hide_decoration = True # Causes issues with aerospace tiling https://github.com/nikitabobko/AeroSpace/issues/276

# Layout
c.scrolling.bar = "when-searching"
c.statusbar.show = "in-mode"
c.tabs.show = "switching"
c.tabs.last_close = "close"
# c.tabs.new_position.related = "last"

# Downloads
c.downloads.location.directory = "~/Downloads"
c.downloads.remove_finished = 5000
c.downloads.position = "bottom"
c.downloads.location.suggestion = "both"

# Dark mode
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = "dark"
c.qt.args = ["force-dark-mode", "dark-mode-settings"]

# File handling
# c.fileselect.handler = "external"
# c.fileselect.single_file.command = [terminal, "-e", "ranger", "--choosefile", "{}"]
# c.fileselect.multiple_files.command = [terminal, "-e", "ranger", "--choosefiles", "{}"]

# Colors
accent = "#1688f0"
blue = "#0f1d91"
black = "#000000"
white = "#dddddd"
red = "#dd2206"
green = "#3ed500"
yellow = "#f1c200"
purple = "#390d91"

c.colors.completion.category.bg = (
    "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #111)"
)

c.colors.completion.category.border.bottom = accent
c.colors.completion.category.border.top = accent
c.colors.completion.category.fg = accent
c.colors.completion.even.bg = black
c.colors.completion.fg = white
c.colors.completion.item.selected.bg = accent
c.colors.completion.item.selected.fg = black
c.colors.completion.item.selected.match.fg = white
c.colors.completion.match.fg = accent
c.colors.completion.odd.bg = black
c.colors.completion.scrollbar.fg = white
c.colors.downloads.bar.bg = black
c.colors.downloads.error.bg = red
c.colors.hints.bg = black
c.colors.hints.fg = white
c.colors.hints.match.fg = green
c.colors.messages.info.bg = black
c.colors.statusbar.command.bg = black
c.colors.statusbar.insert.bg = accent
c.colors.statusbar.insert.fg = white
c.colors.statusbar.normal.bg = black
c.colors.statusbar.passthrough.bg = purple
c.colors.statusbar.private.bg = yellow
c.colors.statusbar.url.fg = accent
c.colors.statusbar.url.warn.fg = yellow
c.colors.tabs.bar.bg = black
c.colors.tabs.even.bg = black
c.colors.tabs.odd.bg = black
c.colors.tabs.pinned.even.bg = blue
c.colors.tabs.pinned.odd.bg = blue
c.colors.tabs.pinned.selected.even.bg = accent
c.colors.tabs.pinned.selected.odd.bg = accent
c.colors.tabs.selected.even.bg = accent
c.colors.tabs.selected.odd.bg = accent

# Font
font_size = "12pt"
font_family = "FiraCode Nerd Font"
font = font_size + " " + font_family
c.fonts.default_size = font_size
c.fonts.default_family = font_family
c.fonts.completion.entry = font
c.fonts.hints = font
c.fonts.debug_console = font
c.fonts.prompts = font
c.fonts.statusbar = font

# Home page
c.url.default_page = homepage
c.url.start_pages = homepage

# Search engines
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "am": "https://amazon.com/s?k={}",
    "aw": "https://wiki.archlinux.org/?search={}",
    "bn": "https://bing.com/search?q={}",
    "dd": "https://duckduckgo.com/?q={}",
    "gh": "https://github.com/search?q={}",
    "gg": "https://google.com/search?q={}",
    "gho": "https://github.com/{}",
    "ghr": "https://github.com/" + username + "/{}",
    "jr": "https://healthsparq.atlassian.net/browse/{}",
    "mp": "https://google.com/maps?q={}",
    "rd": "https://reddit.com/search/?q={}",
    "rds": "https://reddit.com/r/{}",
    "rt": "https://rottentomatoes.com/search?search={}",
    "so": "https://stackoverflow.com/search?q={}",
    "sp": "https://open.spotify.com/search/{}",
    "tw": "https://twitter.com/search?q={}",
    "ud": "https://urbandictionary.com/define.php?term={}",
    "wk": "https://en.wikipedia.org/wiki/{}",
    "yt": "https://youtube.com/results?search_query={}",
    "ytm": "https://music.youtube.com/search?q={}",
}

# Aliases
c.aliases = {
    "o": "open",
    "q": "quit",
    "Q": "close",
    "w": "session-save",
    "x": "quit --save",
}

# Keybindings
config.bind("H", "tab-prev")
config.bind("J", "forward")
config.bind("K", "back")
config.bind("L", "tab-next")
config.bind("O", "cmd-set-text -s :open -w")
config.bind("P", "cmd-set-text -s :open -p")
config.bind("Q", "close")
config.bind("W", "tab-clone -w")
config.bind("a", "mode-enter insert")
config.bind("t", "cmd-set-text -s :open -t")

config.bind("<Ctrl-=>", "zoom-in")
config.bind("<Ctrl-->", "zoom-out")
config.bind("<Meta-=>", "zoom-in")
config.bind("<Meta-->", "zoom-out")

config.bind(leader + "cb", "config-cycle statusbar.show always in-mode")
config.bind(leader + "ce", "config-edit")
config.bind(leader + "ch", "help")
config.bind(leader + "ci", "open -t https://github.com/2kabhishek/qute2k")
config.bind(leader + "cr", "config-source")
config.bind(leader + "cs", "cmd-set-text -s :set -t")
config.bind(leader + "ct", "config-cycle tabs.show multiple switching")

config.bind(leader + "dd", "devtools")
config.bind(leader + "de", "edit-text")
config.bind(leader + "dc", "cmd-edit")
config.bind(leader + "df", "devtools-focus")
config.bind(leader + "dp", "screenshot " + ss_dir + "qute-" + timestamp + ".png")
config.bind(leader + "ds", "view-source --edit")

config.bind(leader + "fc", "hint links yank --rapid")
config.bind(leader + "fd", "hint links spawn " + terminal + "-e youtube-dl {hint-url}")
config.bind(leader + "fh", "hint links tab-bg --rapid")
config.bind(leader + "fi", "hint inputs")
config.bind(leader + "fo", "hint links window")
config.bind(leader + "fp", "hint links run :open -p {hint-url}")
config.bind(leader + "fv", "hint links spawn mpv {hint-url}")
config.bind(leader + "fy", "hint links yank")

config.bind(leader + "qa", "close")
config.bind(leader + "qq", "tab-close")
config.bind(leader + "qr", "restart")
config.bind(leader + "qt", "tab-only")
config.bind(leader + "qw", "window-only")

config.bind(leader + "ta", "bookmark-add")
config.bind(leader + "tb", "bookmark-list")
config.bind(leader + "tc", "tab-clone")
config.bind(leader + "td", "tab-clone -w")
config.bind(leader + "tg", "tab-give")
config.bind(leader + "th", "history")
config.bind(leader + "tm", "cmd-set-text -s :tab-move")
config.bind(leader + "tp", "tab-pin")
config.bind(leader + "tt", "cmd-set-text -s :tab-select")
config.bind(leader + "tu", "undo")
config.bind(leader + "tw", "cmd-set-text -s :tab-take")

config.bind(leader + "x", "quit --save")
