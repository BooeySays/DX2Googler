#!/usr/bin/env python3

import shutil
import os

COLUMNS, LINES = shutil.get_terminal_size()
SEARCHRESULTS = int((LINES - 4) / 5)
__version__='0.3.1'
BARSTRING = "  Enter your search query + Press [ENTER]"

LID = COLUMNS - 2
BAR = COLUMNS - 18
print('\n\033[m' + '╭' + '─' * LID + '╮' + '\n\n' + '╰' + '─' * LID + '╯')
# Original search bar where the color of the bar
# is just color reset, reversed
#
#searchq = input('\033[2A\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[m' + '\033[07m' + ' ' * BAR + '\033[m ' + '│' + '\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[m' + '\033[07m ')
#
# Search bar Modified v2:
# The color is set to 38;5;15m, reversed
#
#searchq = input('\033[2A\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[m' + '\033[07;38;5;15m' + ' ' * BAR + '\033[m ' + '│' + '\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[00;38;5;15m' + '\033[07m ')
# Search bar Modified v3:
# The color is set to 38;5;15m, reversed, with string in box in light grey
# #Cursor is also OFF
#
#print('\033[?23l')
searchq = input('\033[2A\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[m' + '\033[00;03;07;38;5;15m' + '\033[48;5;252m' + BARSTRING + '\033[00;07;38;5;15m' + ' ' * (BAR - len(BARSTRING)) + '\033[m ' + '│' + '\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[00;38;5;15m' + '\033[07m ')
print('\033[m\n')
# Modified to turn cursor back on
#print('\033[m\033[?23h\n')
print('\033[m     Showing results for: "\033[01;38;5;51m' + searchq + '\033[m"')
os.system('dx2googler --colors BmcgxX -n ' + str(SEARCHRESULTS) + ' ' + searchq)
