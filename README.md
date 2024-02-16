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
ln -sfnv $PWD/qute2k $HOME/qutebrowser
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

| Shortcut                       | Action                       | Command                        |
| ------------------------------ | ---------------------------- | ------------------------------ |
| <kbd>a</kbd>                   | Enter insert mode            | `mode-enter insert`            |
| <kbd>t</kbd>                   | Open in new tab              | `cmd-set-text -s :open -t`     |
| <kbd>O</kbd>                   | Open in new window           | `cmd-set-text -s :open -w`     |
| <kbd>P</kbd>                   | Open in private window       | `cmd-set-text -s :open -p`     |
| <kbd>W</kbd>                   | Cline tab in new window      | `tab-give -w`                  |
| <kbd>H</kbd>                   | Switch to the previous tab   | `tab-prev`                     |
| <kbd>L</kbd>                   | Switch to the next tab       | `tab-next`                     |
| <kbd>K</kbd>                   | Go back in history           | `back`                         |
| <kbd>J</kbd>                   | Go forward in history        | `forward`                      |
| <kbd>Ctrl-+</kbd>              | Zoom in                      | `zoom-in`                      |
| <kbd>Ctrl--</kbd>              | Zoom out                     | `zoom-out`                     |
| <kbd>Leader</kbd> <kbd>b</kbd> | Toggle status bar visibility | `config-cycle statusbar.show ` |
| <kbd>Leader</kbd> <kbd>B</kbd> | Toggle tab bar visibility    | `config-cycle tabs.show `      |
| <kbd>Leader</kbd> <kbd>c</kbd> | Edit configuration file      | `config-edit`                  |
| <kbd>Leader</kbd> <kbd>C</kbd> | Set command in command mode  | `cmd-set-text -s :set -t`      |
| <kbd>Leader</kbd> <kbd>d</kbd> | Open devtools                | `devtools`                     |
| <kbd>Leader</kbd> <kbd>D</kbd> | Focus on devtools            | `devtools-focus`               |
| <kbd>Leader</kbd> <kbd>e</kbd> | Edit text                    | `edit-text`                    |
| <kbd>Leader</kbd> <kbd>E</kbd> | Edit command in $EDITOR      | `cmd-edit`                     |
| <kbd>Leader</kbd> <kbd>f</kbd> | Open multiple links          | `edit-text`                    |
| <kbd>Leader</kbd> <kbd>h</kbd> | View history                 | `history`                      |
| <kbd>Leader</kbd> <kbd>H</kbd> | Open help page               | `help`                         |
| <kbd>Leader</kbd> <kbd>i</kbd> | Activate hints for inputs    | `hint inputs`                  |
| <kbd>Leader</kbd> <kbd>I</kbd> | Open this help               | `open -t` repo_url             |
| <kbd>Leader</kbd> <kbd>m</kbd> | List bookmarks               | `bookmark-list`                |
| <kbd>Leader</kbd> <kbd>M</kbd> | Add bookmark                 | `bookmark-add`                 |
| <kbd>Leader</kbd> <kbd>n</kbd> | Clone current tab            | `tab-clone`                    |
| <kbd>Leader</kbd> <kbd>N</kbd> | Clone tab in new window      | `tab-clone -w`                 |
| <kbd>Leader</kbd> <kbd>o</kbd> | Open link in new window      | `hint links window`            |
| <kbd>Leader</kbd> <kbd>O</kbd> | Open link in private window  | `hint links run :open -p`      |
| <kbd>Leader</kbd> <kbd>p</kbd> | Pin current tab              | `tab-pin`                      |
| <kbd>Leader</kbd> <kbd>P</kbd> | Move tab to a new position   | `cmd-set-text -s :tab-move`    |
| <kbd>Leader</kbd> <kbd>q</kbd> | Close current tab            | `tab-close`                    |
| <kbd>Leader</kbd> <kbd>Q</kbd> | Close the browser            | `close`                        |
| <kbd>Leader</kbd> <kbd>r</kbd> | Reload configuration file    | `config-source`                |
| <kbd>Leader</kbd> <kbd>R</kbd> | Restart the browser          | `restart`                      |
| <kbd>Leader</kbd> <kbd>s</kbd> | Take a screenshot            | `screenshot` + path            |
| <kbd>Leader</kbd> <kbd>S</kbd> | View page source in editor   | `view-source --edit`           |
| <kbd>Leader</kbd> <kbd>t</kbd> | Open tab switcher            | `cmd-set-text -s :tab-select`  |
| <kbd>Leader</kbd> <kbd>T</kbd> | Close other tabs             | `tab-only`                     |
| <kbd>Leader</kbd> <kbd>u</kbd> | Undo last action             | `undo`                         |
| <kbd>Leader</kbd> <kbd>v</kbd> | Open link in mpv             | `hint links spawn` + mpv       |
| <kbd>Leader</kbd> <kbd>V</kbd> | Open link in youtube-dl      | `hint links spawn ` + ytdl     |
| <kbd>Leader</kbd> <kbd>w</kbd> | Open tab in another window   | `tab-give`                     |
| <kbd>Leader</kbd> <kbd>W</kbd> | Take tab from another window | `cmd-set-text -s :tab-take`    |
| <kbd>Leader</kbd> <kbd>y</kbd> | Yank link                    | `hint links yank`              |
| <kbd>Leader</kbd> <kbd>x</kbd> | Quit the browser             | `quit --save`                  |
| <kbd>Leader</kbd> <kbd>X</kbd> | Close other windows          | `window-only`                  |

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
