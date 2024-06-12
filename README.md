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

| Shortcut                       | Action                     | Command                    |
| ------------------------------ | -------------------------- | -------------------------- |
| <kbd>H</kbd>                   | Switch to the previous tab | `tab-prev`                 |
| <kbd>J</kbd>                   | Go forward in history      | `forward`                  |
| <kbd>K</kbd>                   | Go back in history         | `back`                     |
| <kbd>L</kbd>                   | Switch to the next tab     | `tab-next`                 |
| <kbd>O</kbd>                   | Open in new window         | `cmd-set-text -s :open -w` |
| <kbd>P</kbd>                   | Open in private window     | `cmd-set-text -s :open -p` |
| <kbd>Q</kbd>                   | Close the browser          | `close`                    |
| <kbd>W</kbd>                   | Clone tab in new window    | `tab-clone -w`             |
| <kbd>a</kbd>                   | Enter insert mode          | `mode-enter insert`        |
| <kbd>t</kbd>                   | Open in new tab            | `cmd-set-text -s :open -t` |
| <kbd>Ctrl-+</kbd>              | Zoom in                    | `zoom-in`                  |
| <kbd>Ctrl--</kbd>              | Zoom out                   | `zoom-out`                 |
| <kbd>Meta-+</kbd>              | Zoom in                    | `zoom-in`                  |
| <kbd>Meta--</kbd>              | Zoom out                   | `zoom-out`                 |
| <kbd>Leader</kbd> <kbd>x</kbd> | Quit the browser           | `quit --save`              |

#### Config Bindings

| Shortcut                        | Action                       | Command                                        |
| ------------------------------- | ---------------------------- | ---------------------------------------------- |
| <kbd>Leader</kbd> <kbd>cb</kbd> | Toggle status bar visibility | `config-cycle statusbar.show always in-mode`   |
| <kbd>Leader</kbd> <kbd>ce</kbd> | Edit configuration file      | `config-edit`                                  |
| <kbd>Leader</kbd> <kbd>ch</kbd> | Open help page               | `help`                                         |
| <kbd>Leader</kbd> <kbd>ci</kbd> | Open GitHub page in new tab  | `open -t https://github.com/2kabhishek/qute2k` |
| <kbd>Leader</kbd> <kbd>cr</kbd> | Reload configuration file    | `config-source`                                |
| <kbd>Leader</kbd> <kbd>cs</kbd> | Set command in command mode  | `cmd-set-text -s :set -t`                      |
| <kbd>Leader</kbd> <kbd>ct</kbd> | Toggle tab bar visibility    | `config-cycle tabs.show multiple switching`    |

#### Developer Bindings

| Shortcut                        | Action                     | Command              |
| ------------------------------- | -------------------------- | -------------------- |
| <kbd>Leader</kbd> <kbd>dd</kbd> | Open devtools              | `devtools`           |
| <kbd>Leader</kbd> <kbd>de</kbd> | Edit text                  | `edit-text`          |
| <kbd>Leader</kbd> <kbd>dc</kbd> | Edit command in $EDITOR    | `cmd-edit`           |
| <kbd>Leader</kbd> <kbd>df</kbd> | Focus on devtools          | `devtools-focus`     |
| <kbd>Leader</kbd> <kbd>dp</kbd> | Take a screenshot          | `screenshot` + path  |
| <kbd>Leader</kbd> <kbd>ds</kbd> | View page source in editor | `view-source --edit` |

#### Hints Bindings

| Shortcut                        | Action                          | Command                     |
| ------------------------------- | ------------------------------- | --------------------------- |
| <kbd>Leader</kbd> <kbd>fc</kbd> | Yank link                       | `hint links yank --rapid`   |
| <kbd>Leader</kbd> <kbd>fd</kbd> | Download video with youtube-dl  | `hint links spawn` + ytdl   |
| <kbd>Leader</kbd> <kbd>fh</kbd> | Open link in new background tab | `hint links tab-bg --rapid` |
| <kbd>Leader</kbd> <kbd>fi</kbd> | Activate hints for inputs       | `hint inputs`               |
| <kbd>Leader</kbd> <kbd>fo</kbd> | Open link in new window         | `hint links window`         |
| <kbd>Leader</kbd> <kbd>fp</kbd> | Open link in private window     | `hint links run :open -p`   |
| <kbd>Leader</kbd> <kbd>fv</kbd> | Open link in mpv                | `hint links spawn mpv`      |
| <kbd>Leader</kbd> <kbd>fy</kbd> | Yank link                       | `hint links yank`           |

#### Quit Bindings

| Shortcut                        | Action              | Command       |
| ------------------------------- | ------------------- | ------------- |
| <kbd>Leader</kbd> <kbd>qa</kbd> | Close the browser   | `close`       |
| <kbd>Leader</kbd> <kbd>qq</kbd> | Close current tab   | `tab-close`   |
| <kbd>Leader</kbd> <kbd>qr</kbd> | Restart the browser | `restart`     |
| <kbd>Leader</kbd> <kbd>qt</kbd> | Close other tabs    | `tab-only`    |
| <kbd>Leader</kbd> <kbd>qw</kbd> | Close other windows | `window-only` |

#### Tab Bindings

| Shortcut                        | Action                       | Command                       |
| ------------------------------- | ---------------------------- | ----------------------------- |
| <kbd>Leader</kbd> <kbd>ta</kbd> | Add bookmark                 | `bookmark-add`                |
| <kbd>Leader</kbd> <kbd>tb</kbd> | List bookmarks               | `bookmark-list`               |
| <kbd>Leader</kbd> <kbd>tc</kbd> | Clone current tab            | `tab-clone`                   |
| <kbd>Leader</kbd> <kbd>td</kbd> | Clone tab in new window      | `tab-clone -w`                |
| <kbd>Leader</kbd> <kbd>tg</kbd> | Give tab to another window   | `tab-give`                    |
| <kbd>Leader</kbd> <kbd>th</kbd> | View history                 | `history`                     |
| <kbd>Leader</kbd> <kbd>tm</kbd> | Move tab to a new position   | `cmd-set-text -s :tab-move`   |
| <kbd>Leader</kbd> <kbd>tp</kbd> | Pin current tab              | `tab-pin`                     |
| <kbd>Leader</kbd> <kbd>tt</kbd> | Open tab switcher            | `cmd-set-text -s :tab-select` |
| <kbd>Leader</kbd> <kbd>tu</kbd> | Undo last action             | `undo`                        |
| <kbd>Leader</kbd> <kbd>tw</kbd> | Take tab from another window | `cmd-set-text -s :tab-take`   |

To edit keybindings visit: [config.py](./config.py)

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
