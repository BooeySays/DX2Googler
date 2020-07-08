#!/usr/bin/env python3

import shutil

_VERSION_ = "1.1"

COLS, LINES = shutil.get_terminal_size()

BGB = "\033[07m \033[m"
GOOGLELOGO = "\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;00m: \033[1C\033[48;5;252m"
BG = "\033[48;5;252m \033[m"

print("\n")
print(" " + BG * (COLS - 2) + "\n " + BG + BGB * (COLS - 4) + BG + "\n " + BG * (COLS - 2) + "\n\r\033[2A\033[2C" + "\033[48;5;252m " + GOOGLELOGO + "\033[0m\033[7m", end="")
eee = input("")
print("\033[m\n\n")
#print()
#Ｇｏｏｇｌｅ
