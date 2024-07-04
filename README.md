<div align = "center">

<h1><a href="https://github.com/2kabhishek/qute2k">qute2k</a></h1>

<a href="https://github.com/2KAbhishek/qute2k/blob/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/2kabhishek/qute2k?style=flat&color=eee&label="> </a>

<a href="https://github.com/2KAbhishek/qute2k/graphs/contributors">
<img alt="People" src="https://img.shields.io/github/contributors/2kabhishek/qute2k?style=flat&color=ffaaf2&label=People"> </a>

<a href="https://github.com/2KAbhishek/qute2k/stargazers">
<img alt="Stars" src="https://img.shields.io/github/stars/2kabhishek/qute2k?style=flat&color=98c379&label=Stars"></a>

<a href="https://github.com/2KAbhishek/qute2k/network/members">
<img alt="Forks" src="https://img.shields.io/github/forks/2kabhishek/qute2k?style=flat&color=66a8e0&label=Forks"> </a>

<a href="https://github.com/2KAbhishek/qute2k/watchers">
<img alt="Watches" src="https://img.shields.io/github/watchers/2kabhishek/qute2k?style=flat&color=f5d08b&label=Watches"> </a>

<a href="https://github.com/2KAbhishek/qute2k/pulse">
<img alt="Last Updated" src="https://img.shields.io/github/last-commit/2kabhishek/qute2k?style=flat&color=e06c75&label="> </a>

<h3>The fastest and qutest browser 🌐🩷</h3>

<figure>
  <img src="images/screenshot.png" alt="qute2k in action">
  <br/>
  <figcaption>qute2k in action</figcaption>
</figure>

</div>

qute2k is a [qutebrowser](https://qutebrowser.org/) config that aims to make the browser fully keyboard navigable.

## ✨ Features

- Sane and easily expandable configs
- Logical keybindings, inspired by vim ([nvim2k](https://github.com/2kabhishek/nvim2k))

## ⚡ Setup

### ⚙️ Requirements

- 'qutebrowser' 3.0+

### 💻 Installation

Installation is as simple as cloning and symlinking

```bash
# Clone Repo
git clone https://github.com/2kabhishek/qute2k
```

```bash
# On Linux
ln -sfnv $PWD/qute2k $HOME/.config/qutebrowser
```

```bash
# On Mac
ln -sfnv $PWD/qute2k $HOME/.qutebrowser
```

```powershell
# On Windows
New-Item -ItemType SymbolicLink -Path "$env:APPDATA\qutebrowser\config" -Target "$PWD\qute2k" -Force
```

## 🚀 Usage

Launch qutebrowser after finishing installation steps.

Update variables section in [config.py](./config.py) according to your needs.

Use vim keybindings and ex (`:`) commands for various actions.

### ⌨️ Keybindings

This table contains all the custom keybindings added by qute2k, find [default qutebrowser bindings here](qute://help/img/cheatsheet-big.png)

> Leader is mapped to `Space` by default

#### Generic Bindings

| Shortcut                       | Action                     |
| ------------------------------ | -------------------------- |
| <kbd>H</kbd>                   | Switch to the previous tab |
| <kbd>J</kbd>                   | Go forward in history      |
| <kbd>K</kbd>                   | Go back in history         |
| <kbd>L</kbd>                   | Switch to the next tab     |
| <kbd>O</kbd>                   | Open in new window         |
| <kbd>P</kbd>                   | Open in private window     |
| <kbd>Q</kbd>                   | Close the browser          |
| <kbd>W</kbd>                   | Clone tab in new window    |
| <kbd>a</kbd>                   | Enter insert mode          |
| <kbd>t</kbd>                   | Open in new tab            |
| <kbd>Ctrl-+</kbd>              | Zoom in                    |
| <kbd>Ctrl--</kbd>              | Zoom out                   |
| <kbd>Meta-+</kbd>              | Zoom in                    |
| <kbd>Meta--</kbd>              | Zoom out                   |
| <kbd>Leader</kbd> <kbd>x</kbd> | Quit the browser           |

#### Config Bindings

| Shortcut                        | Action                       |
| ------------------------------- | ---------------------------- |
| <kbd>Leader</kbd> <kbd>cb</kbd> | Toggle status bar visibility |
| <kbd>Leader</kbd> <kbd>cc</kbd> | Edit configuration file      |
| <kbd>Leader</kbd> <kbd>ch</kbd> | Open help page               |
| <kbd>Leader</kbd> <kbd>ci</kbd> | Open GitHub page in new tab  |
| <kbd>Leader</kbd> <kbd>cr</kbd> | Reload configuration file    |
| <kbd>Leader</kbd> <kbd>cs</kbd> | Set command in command mode  |
| <kbd>Leader</kbd> <kbd>ct</kbd> | Toggle tab bar visibility    |

#### Developer Bindings

| Shortcut                        | Action                     |
| ------------------------------- | -------------------------- |
| <kbd>Leader</kbd> <kbd>dd</kbd> | Open devtools              |
| <kbd>Leader</kbd> <kbd>de</kbd> | Edit text                  |
| <kbd>Leader</kbd> <kbd>dc</kbd> | Edit command in $EDITOR    |
| <kbd>Leader</kbd> <kbd>df</kbd> | Focus on devtools          |
| <kbd>Leader</kbd> <kbd>dp</kbd> | Take a screenshot          |
| <kbd>Leader</kbd> <kbd>ds</kbd> | View page source in editor |

#### Hints Bindings

| Shortcut                        | Action                          |
| ------------------------------- | ------------------------------- |
| <kbd>Leader</kbd> <kbd>fc</kbd> | Yank link                       |
| <kbd>Leader</kbd> <kbd>fd</kbd> | Download video with youtube-dl  |
| <kbd>Leader</kbd> <kbd>ff</kbd> | Open link in new background tab |
| <kbd>Leader</kbd> <kbd>fi</kbd> | Activate hints for inputs       |
| <kbd>Leader</kbd> <kbd>fo</kbd> | Open link in new window         |
| <kbd>Leader</kbd> <kbd>fp</kbd> | Open link in private window     |
| <kbd>Leader</kbd> <kbd>fv</kbd> | Open link in mpv                |
| <kbd>Leader</kbd> <kbd>fy</kbd> | Yank link                       |

#### Quit Bindings

| Shortcut                        | Action              |
| ------------------------------- | ------------------- |
| <kbd>Leader</kbd> <kbd>qd</kbd> | Close current tab   |
| <kbd>Leader</kbd> <kbd>qq</kbd> | Close the browser   |
| <kbd>Leader</kbd> <kbd>qr</kbd> | Restart the browser |
| <kbd>Leader</kbd> <kbd>qt</kbd> | Close other tabs    |
| <kbd>Leader</kbd> <kbd>qw</kbd> | Close other windows |

#### Tab Bindings

| Shortcut                        | Action                       |
| ------------------------------- | ---------------------------- |
| <kbd>Leader</kbd> <kbd>ta</kbd> | Add bookmark                 |
| <kbd>Leader</kbd> <kbd>tb</kbd> | List bookmarks               |
| <kbd>Leader</kbd> <kbd>tc</kbd> | Clone current tab            |
| <kbd>Leader</kbd> <kbd>td</kbd> | Clone tab in new window      |
| <kbd>Leader</kbd> <kbd>tg</kbd> | Give tab to another window   |
| <kbd>Leader</kbd> <kbd>th</kbd> | View history                 |
| <kbd>Leader</kbd> <kbd>tm</kbd> | Move tab to a new position   |
| <kbd>Leader</kbd> <kbd>tp</kbd> | Pin current tab              |
| <kbd>Leader</kbd> <kbd>tt</kbd> | Open tab switcher            |
| <kbd>Leader</kbd> <kbd>tu</kbd> | Undo last action             |
| <kbd>Leader</kbd> <kbd>tw</kbd> | Take tab from another window |

To edit keybindings visit: [config.py](./config.py)

### 🔎 Search Engines

| Keybinding         | Action                                                             |
| ------------------ | ------------------------------------------------------------------ |
| <key>DEFAULT</key> | [DuckDuckGo](https://duckduckgo.com/?q={})                         |
| <key>am</key>      | [Amazon](https://amazon.com/s?k={})                                |
| <key>aw</key>      | [Arch Linux](https://wiki.archlinux.org/?search={})                |
| <key>bn</key>      | [Bing](https://bing.com/search?q={})                               |
| <key>dd</key>      | [DuckDuckGo](https://duckduckgo.com/?q={})                         |
| <key>gg</key>      | [Google](https://google.com/search?q={})                           |
| <key>gh</key>      | [GitHub](https://github.com/search?q={})                           |
| <key>gho</key>     | [GitHub Open](https://github.com/{})                               |
| <key>ghp</key>     | [GitHub PRs](https://www.github.com/pulls)                         |
| <key>ghr</key>     | [GitHub Repo](https://github.com/2kabhishek/{})                    |
| <key>jr</key>      | [JIRA Ticket](https://healthsparq.atlassian.net/browse/{})         |
| <key>mp</key>      | [Google Maps](https://google.com/maps?q={})                        |
| <key>rd</key>      | [Reddit](https://reddit.com/search/?q={})                          |
| <key>rds</key>     | [Reddit Sub](https://reddit.com/r/{})                              |
| <key>rt</key>      | [Rotten Tomatoes](https://rottentomatoes.com/search?search={})     |
| <key>so</key>      | [Stack Overflow](https://stackoverflow.com/search?q={})            |
| <key>sp</key>      | [Spotify](https://open.spotify.com/search/{})                      |
| <key>tw</key>      | [Twitter](https://twitter.com/search?q={})                         |
| <key>ud</key>      | [Urban Dictionary](https://urbandictionary.com/define.php?term={}) |
| <key>wk</key>      | [Wikipedia](https://en.wikipedia.org/wiki/{})                      |
| <key>yt</key>      | [YouTube](https://youtube.com/results?search_query={})             |
| <key>ytm</key>     | [YouTube Music](https://music.youtube.com/search?q={})             |

## 🧑‍💻 Behind The Code

### 🌈 Inspiration

I have always wanted a mouse less workflow, but the browser was always a blocker, qute2k fixes it!!

### 💡 Challenges/Learnings

- The initial configuration process involved a lot of docs, but was worth it.

### 🧰 Tooling

- [dots2k](https://github.com/2kabhishek/dots2k) — Dev Environment
- [nvim2k](https://github.com/2kabhishek/nvim2k) — Personalized Editor
- [sway2k](https://github.com/2kabhishek/sway2k) — Desktop Environment

<hr>

<div align="center">

<strong>⭐ hit the star button if you found this useful ⭐</strong><br>

<a href="https://github.com/2KAbhishek/qute2k">Source</a>
| <a href="https://2kabhishek.github.io/blog" target="_blank">Blog </a>
| <a href="https://twitter.com/2kabhishek" target="_blank">Twitter </a>
| <a href="https://linkedin.com/in/2kabhishek" target="_blank">LinkedIn </a>
| <a href="https://2kabhishek.github.io/links" target="_blank">More Links </a>
| <a href="https://2kabhishek.github.io/projects" target="_blank">Other Projects </a>

</div>
