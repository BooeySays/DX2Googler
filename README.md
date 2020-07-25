<p align="center">
<a href="https://github.com/jarun/googler/releases/latest"><img src="https://img.shields.io/github/release/jarun/googler.svg?maxAge=600" alt="Latest release" /></a>
<a href="https://aur.archlinux.org/packages/googler"><img src="https://img.shields.io/aur/version/googler.svg?maxAge=600" alt="AUR" /></a>
<a href="http://formulae.brew.sh/formula/googler"><img src="https://img.shields.io/homebrew/v/googler.svg?maxAge=600" alt="Homebrew" /></a>
<a href="https://packages.debian.org/search?keywords=googler&searchon=names"><img src="https://img.shields.io/badge/debian-9+-blue.svg?maxAge=2592000" alt="Debian Stretch+" /></a>
<a href="https://apps.fedoraproject.org/packages/googler"><img src="https://img.shields.io/badge/fedora-27+-blue.svg?maxAge=2592000" alt="Fedora 27+" /></a>
<a href="https://software.opensuse.org/search?q=googler"><img src="https://img.shields.io/badge/opensuse%20leap-15.0+-blue.svg?maxAge=2592000" alt="openSUSE Leap 15.0+" /></a>
<a href="https://packages.ubuntu.com/search?keywords=googler&searchon=names"><img src="https://img.shields.io/badge/ubuntu-16.10+-blue.svg?maxAge=2592000" alt="Ubuntu Yakkety+" /></a>
</p>

<p align="center">
<a href="https://repology.org/metapackage/googler"><img src="https://repology.org/badge/tiny-repos/googler.svg" alt="Availability"></a>
<a href="https://github.com/jarun/googler/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-GPLv3-yellow.svg?maxAge=2592000" alt="License" /></a>
<a href="https://circleci.com/gh/jarun/workflows/googler"><img src="https://img.shields.io/circleci/project/github/jarun/googler.svg" alt="Build Status" /></a>
</p>

<p align="center">
<a href="https://asciinema.org/a/vyvNa0mg0zcBOfiNZUVJaIT1M" target="_blank"><img src="https://asciinema.org/a/vyvNa0mg0zcBOfiNZUVJaIT1M.svg" /></a>
</p>

`DX2Googler` is my take on `googler` (https://github.com/jarun/googler) is a power tool to Google (Web & News) and Google Site Search from the command-line. It shows the title, URL and abstract for each result, which can be directly opened in a browser from the terminal. Results are fetched in pages (with page navigation). Supports sequential searches in a single `googler` instance.

I originally started working on `DX2Googler` because I wanted using `googler` to have a feel more similar to using Google from a web browser. That, and I wanted to simplify the process, instead of having to type a huge command line just to do a simple search.

To do this, I added the following:
  - A few different input screens to choose from, including one that looks like the main Google.com webpage (with colored Google logo, input box, and non-functioning buttons)
  - Edit'd googler's prompts here and there, adding alot more color to make things alot easier to look at
  - Automatically set the output colors to match Google's default color theme
  - Automatically set the number of result to display argument by taking into account the terminals current size and figuring out how many results would fit on the screen
  - Added a HOTKEY option ([CTRL] + [k]), just like the search hotkey used for most GUI web browsers out there (except MS Edge, which used a different key combination)
  
<b>INSTALLATION:</b><br>
  1. After cloning this repo, navigate into the directory and execute the install.sh script<br>
    1a. <b>DX2Googler</b> requires that the terminal be set up with <b>DX2Setup</b> <i>(A script I made that will set up a system to make it easier to install and uninstall add-ons, keeping it totally separate)</i>, so it will search to see if <b>DX2Setup</b> is installed. If not, it will prompt to install it.

<b>CONFIGURATION:</b><br>
  1. After install, you can change the theme (the Google search screen) by running the command, `dx2googler-theme` from anywhere in the terminal.<br><br>
`DX2Googler` isn't affiliated to Google in any way.

For more information about `googler` (including all of its functions, arguments, etc), check out its README.md at https://github.com/jarun/googler
