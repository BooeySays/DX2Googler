#!/usr/bin/env python3

import shutil
import os

_VERSION_ = "1.4"

COLS, LINES = shutil.get_terminal_size()
SEARCHRESULTS = int((LINES - 4) / 5.3)
BGB = "\033[48;5;252m \033[m"
GOOGLELOGO = "\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;00m: \033[1C\033[48;5;252m"
BG = "\033[48;5;15m \033[m"
SEARCHBUTTON = "\033[m\033[48;5;15m \033[48;5;252m\033[38;5;00m SEARCH \033[m\033[48;5;15m \033[m"

print("\n")
print(" " + BG * (COLS - 2) + "\n " + BG + BGB * (COLS - 4) + BG + "\033[10D" + SEARCHBUTTON + "\n " + BG * (COLS - 2) + "\n\r\033[2A\033[2C" + "\033[48;5;15m " + GOOGLELOGO + "\033[0m", end="")
searchq = input("\033[38;5;00m\033[48;5;252m")
print("\033[m\n\n")

os.system('dx2googler --colors BmcgxX -n ' + str(SEARCHRESULTS) + ' ' + searchq)

#print()
#Ｇｏｏｇｌｅ

##	CHANGELOG
#
#	v1.4
#	  -	Changed SEARCHRESULT equation - divide by 5.3 instead of 5
#
#	v1.3
#	  -	Imported os
#	  -	added SEARCHRESULTS to calculate how many search results the
#		current screen size can display
#	  -	Added os.system at the end to execute dx2googler, plugging in
#		the users input and SEARCHRESULTS
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
