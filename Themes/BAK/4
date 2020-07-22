#!/usr/bin/env python3

# DESC:	Draws:
#	  -	Google
#	  -	Font	= smmono9
#	  -	Colors	= Yes - Google theme colors
#	  -	Format	= Centered
#	  -	Width	= 60
#	  -	Height	= 9
#

import shutil
import os

COLS, LINES = shutil.get_terminal_size()
CENTEREDSPACES = int((COLS - 60) / 2)
SEARCHRESULTS = int((LINES - 4) / 5.2)

BUTTONSEARCH = "[m[38;5;00m[48;5;252m Google Search [m"		# 15 wide
BUTTONLUCKY = "[m[38;5;00m[48;5;252m I'm Feeling Lucky [m"	# 19 wide
BUTTONLINE = (BUTTONSEARCH + "\033[m " + BUTTONLUCKY)			# 35 wide
GOOGLELOGO1 = "[38;5;32m          [38;5;160m          [38;5;215m          [38;5;32m          [38;5;34m         [38;5;160m           "
GOOGLELOGO2 = "[38;5;32m    ▄▄▄▄  [38;5;160m          [38;5;215m          [38;5;32m          [38;5;34m ▄▄▄▄    [38;5;160m           "
GOOGLELOGO3 = "[38;5;32m  ██▀▀▀▀█ [38;5;160m          [38;5;215m          [38;5;32m          [38;5;34m ▀▀██    [38;5;160m           "
GOOGLELOGO4 = "[38;5;32m ██       [38;5;160m  ▄████▄  [38;5;215m  ▄████▄  [38;5;32m  ▄███▄██ [38;5;34m   ██    [38;5;160m   ▄████▄  "
GOOGLELOGO5 = "[38;5;32m ██  ▄▄▄▄ [38;5;160m ██▀  ▀██ [38;5;215m ██▀  ▀██ [38;5;32m ██▀  ▀██ [38;5;34m   ██    [38;5;160m  ██▄▄▄▄██ "
GOOGLELOGO6 = "[38;5;32m ██  ▀▀██ [38;5;160m ██    ██ [38;5;215m ██    ██ [38;5;32m ██    ██ [38;5;34m   ██    [38;5;160m  ██▀▀▀▀▀▀ "
GOOGLELOGO7 = "[38;5;32m  ██▄▄▄██ [38;5;160m ▀██▄▄██▀ [38;5;215m ▀██▄▄██▀ [38;5;32m ▀██▄▄███ [38;5;34m   ██▄▄▄ [38;5;160m  ▀██▄▄▄▄█ "
GOOGLELOGO8 = "[38;5;32m    ▀▀▀▀  [38;5;160m   ▀▀▀▀   [38;5;215m   ▀▀▀▀   [38;5;32m  ▄▀▀▀ ██ [38;5;34m    ▀▀▀▀ [38;5;160m    ▀▀▀▀▀  "
GOOGLELOGO9 = "[38;5;32m          [38;5;160m          [38;5;215m          [38;5;32m  ▀████▀▀ [38;5;34m         [38;5;160m           "


print("\033c ")
print(" ")
print(" " * CENTEREDSPACES + GOOGLELOGO1)
print(" " * CENTEREDSPACES + GOOGLELOGO2)
print(" " * CENTEREDSPACES + GOOGLELOGO3)
print(" " * CENTEREDSPACES + GOOGLELOGO4)
print(" " * CENTEREDSPACES + GOOGLELOGO5)
print(" " * CENTEREDSPACES + GOOGLELOGO6)
print(" " * CENTEREDSPACES + GOOGLELOGO7)
print(" " * CENTEREDSPACES + GOOGLELOGO8)
print(" " * CENTEREDSPACES + GOOGLELOGO9)
print(" ")
print(" ")
print(" " * int((COLS * .4) / 2) + "\033[48;5;15m \033[m" * int(COLS * .6))
print(" ")
print(" " * int((COLS - 35) / 2) + BUTTONLINE)
searchq = input("\033[3A\033[" + str(int(((COLS * .4) / 2)) + 1) + "C\033[48;5;15m\033[38;5;00m")
print("\033[3B")

os.system('dx2googler --colors BmcgxX -n ' + str(SEARCHRESULTS) + ' ' + searchq)
