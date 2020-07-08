#!/usr/bin/env python3

import shutil

_VERSION_ = "1.2"

COLS, LINES = shutil.get_terminal_size()

BGB = "\033[48;5;15m \033[m"
GOOGLELOGO = "\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;00m: \033[1C\033[48;5;252m"
BG = "\033[48;5;252m \033[m"
SEARCHBUTTON = "\033[m\033[48;5;252m \033[48;5;15m\033[38;5;00m SEARCH \033[m\033[48;5;252m \033[m"

print("\n")
print(" " + BG * (COLS - 2) + "\n " + BG + BGB * (COLS - 4) + BG + "\033[10D" + SEARCHBUTTON + "\n " + BG * (COLS - 2) + "\n\r\033[2A\033[2C" + "\033[48;5;252m " + GOOGLELOGO + "\033[0m\033[7m", end="")
eee = input("")
print("\033[m\n\n")
#print()
#Ｇｏｏｇｌｅ

##	CHANGELOG
#
#	v1.2
#	  -	Added a (non-functioning) search button after the input box
#
#	v1.1
#	  -	Seperated input variable
#
#	v1.0
#	  -	Created new search box without the ascii box border
#