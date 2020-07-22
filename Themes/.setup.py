import os
import sys

DIRDX2 = (os.getenv('DX2') + '/')
DIRHOME = (os.getenv('HOME') + '/')
DIRDX2BIN = (os.getenv('DX2BIN') + '/')
FILEGOOGLECOM = (DIRDX2BIN + 'Google.com')

class files:
	one = (r"""#!/usr/bin/env python3

import shutil
import os

DEFBROWSER = os.getenv("BROWSER")

def getdefaultbrowser():
	defbrowserprompt = "\033[00;01;38;5;51mDefault Browser\033[00;01m: "
	if os.getenv("BROWSER") is None:
		DEFBROW = "\033[00;01;38;5;196mERR\033[00;01m - Default browser is not set"
	else:
		DEFBROW = str.upper(os.getenv("BROWSER"))
	print(defbrowserprompt + DEFBROW)

COLUMNS, LINES = shutil.get_terminal_size()
SEARCHRESULTS = int((LINES - 4) / 5)
__version__='0.3.6.2'
BARSTRING = "  Enter your search query + Press [ENTER]"

LID = COLUMNS - 2
BAR = COLUMNS - 18
print('\n')
getdefaultbrowser()
print('\033[m' + '╭' + '─' * LID + '╮' + '\n\n' + '╰' + '─' * LID + '╯')
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
""")
	two = (r"""#!/usr/bin/env python3

import shutil
import os

_VERSION_ = "1.4"

COLS, LINES = shutil.get_terminal_size()
SEARCHRESULTS = int((LINES - 4) / 5.22222)
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
#	  -	Changed SEARCHRESULT equation - divide by 5.22222 instead of 5
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
""")
	three = (r"""#!/usr/bin/env python3

import shutil
import os

_VERSION_ = "1.4"

COLS, LINES = shutil.get_terminal_size()
SEARCHRESULTS = int((LINES - 4) / 5.22222)
BGB = "\033[48;5;15m \033[m"
GOOGLELOGO = "\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;00m: \033[1C\033[48;5;252m"
BG = "\033[48;5;252m \033[m"
SEARCHBUTTON = "\033[m\033[48;5;252m \033[48;5;15m\033[38;5;00m SEARCH \033[m\033[48;5;252m \033[m"

print("\n")
print(" " + BG * (COLS - 2) + "\n " + BG + BGB * (COLS - 4) + BG + "\033[10D" + SEARCHBUTTON + "\n " + BG * (COLS - 2) + "\n\r\033[2A\033[2C" + "\033[48;5;252m " + GOOGLELOGO + "\033[0m", end="")
searchq = input("\033[38;5;00m\033[48;5;15m")
print("\033[m\n\n")

os.system('dx2googler --colors BmcgxX -n ' + str(SEARCHRESULTS) + ' ' + searchq)

#print()
#Ｇｏｏｇｌｅ

##	CHANGELOG
#
#	v1.4
#	  -	Changed equation - divide by 5.22222 instead of 5
#
#	v1.3
#	  -	imported os
#	  -	added SEARCHRESULTS var which calulates how many search results
#		the current screen size can display
#	  -	added line to plug input and SEARCHRESULTS into execution syntax
#		to use dx2googler
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
""")
	four = (r"""#!/usr/bin/env python3

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
""")

def writefile(x):
	FILE = x
	if os.path.exists(FILEGOOGLECOM) == True:
		os.remove(FILEGOOGLECOM)
	f = open(FILEGOOGLECOM, 'w')
	if FILE == 1:
		f.write(files.one)
	elif FILE == 2:
		f.write(files.two)
	elif FILE == 3:
		f.write(files.three)
	elif FILE == 4:
		f.write(files.four)
	f.close()
	os.system('chmod u+x ' + str(FILEGOOGLECOM))

writefile(4)