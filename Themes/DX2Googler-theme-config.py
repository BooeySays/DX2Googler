#!/usr/bin/env python3

import shutil
import os
import sys


DIRDX2 = (os.getenv('DX2') + '/')
DIRHOME = (os.getenv('HOME') + '/')
DIRDX2BIN = (os.getenv('DX2BIN') + '/')
FILEGOOGLECOM = (DIRDX2BIN + 'Google.com')
DIRDATA = (os.getenv('DX2DATA') + '/dx2googler')

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
GOOGLELOGO1 = "[38;5;32m          [38;5;160m          [38;5;178m          [38;5;32m          [38;5;34m         [38;5;160m           "
GOOGLELOGO2 = "[38;5;32m    ▄▄▄▄  [38;5;160m          [38;5;178m          [38;5;32m          [38;5;34m ▄▄▄▄    [38;5;160m           "
GOOGLELOGO3 = "[38;5;32m  ██▀▀▀▀█ [38;5;160m          [38;5;178m          [38;5;32m          [38;5;34m ▀▀██    [38;5;160m           "
GOOGLELOGO4 = "[38;5;32m ██       [38;5;160m  ▄████▄  [38;5;178m  ▄████▄  [38;5;32m  ▄███▄██ [38;5;34m   ██    [38;5;160m   ▄████▄  "
GOOGLELOGO5 = "[38;5;32m ██  ▄▄▄▄ [38;5;160m ██▀  ▀██ [38;5;178m ██▀  ▀██ [38;5;32m ██▀  ▀██ [38;5;34m   ██    [38;5;160m  ██▄▄▄▄██ "
GOOGLELOGO6 = "[38;5;32m ██  ▀▀██ [38;5;160m ██    ██ [38;5;178m ██    ██ [38;5;32m ██    ██ [38;5;34m   ██    [38;5;160m  ██▀▀▀▀▀▀ "
GOOGLELOGO7 = "[38;5;32m  ██▄▄▄██ [38;5;160m ▀██▄▄██▀ [38;5;178m ▀██▄▄██▀ [38;5;32m ▀██▄▄███ [38;5;34m   ██▄▄▄ [38;5;160m  ▀██▄▄▄▄█ "
GOOGLELOGO8 = "[38;5;32m    ▀▀▀▀  [38;5;160m   ▀▀▀▀   [38;5;178m   ▀▀▀▀   [38;5;32m  ▄▀▀▀ ██ [38;5;34m    ▀▀▀▀ [38;5;160m    ▀▀▀▀▀  "
GOOGLELOGO9 = "[38;5;32m          [38;5;160m          [38;5;178m          [38;5;32m  ▀████▀▀ [38;5;34m         [38;5;160m           "


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

def checkcurrent(x):
	FILE = x
	if os.path.exists(DIRDATA + '/theme.' + str(FILE)) == True:
		print('[00;01;38;5;190m  Currently set theme[m')


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
	if os.path.exists(DIRDATA) == False:
		os.mkdir(DIRDATA)
	os.system('rm ' + str(DIRDATA) + '/theme.*')
	os.system('touch ' + str(DIRDATA) + '/theme.' + str(FILE))



#writefile(4)
##

PWD = os.getenv('PWD')
HOME = os.getenv('HOME')
DEFBROWSER = os.getenv("BROWSER")
BUTTONSEARCHc = "[m[38;5;00m[48;5;252m Google Search [m"		# 15 wide
BUTTONLUCKYc = "[m[38;5;00m[48;5;252m I'm Feeling Lucky [m"	# 19 wide
BUTTONLINEc = (BUTTONSEARCHc + "\033[m " + BUTTONLUCKYc)			# 35 wide
GOOGLELOGO1 = "[38;5;32m          [38;5;160m          [38;5;178m          [38;5;32m          [38;5;34m         [38;5;160m           "
GOOGLELOGO2 = "[38;5;32m    ▄▄▄▄  [38;5;160m          [38;5;178m          [38;5;32m          [38;5;34m ▄▄▄▄    [38;5;160m           "
GOOGLELOGO3 = "[38;5;32m  ██▀▀▀▀█ [38;5;160m          [38;5;178m          [38;5;32m          [38;5;34m ▀▀██    [38;5;160m           "
GOOGLELOGO4 = "[38;5;32m ██       [38;5;160m  ▄████▄  [38;5;178m  ▄████▄  [38;5;32m  ▄███▄██ [38;5;34m   ██    [38;5;160m   ▄████▄  "
GOOGLELOGO5 = "[38;5;32m ██  ▄▄▄▄ [38;5;160m ██▀  ▀██ [38;5;178m ██▀  ▀██ [38;5;32m ██▀  ▀██ [38;5;34m   ██    [38;5;160m  ██▄▄▄▄██ "
GOOGLELOGO6 = "[38;5;32m ██  ▀▀██ [38;5;160m ██    ██ [38;5;178m ██    ██ [38;5;32m ██    ██ [38;5;34m   ██    [38;5;160m  ██▀▀▀▀▀▀ "
GOOGLELOGO7 = "[38;5;32m  ██▄▄▄██ [38;5;160m ▀██▄▄██▀ [38;5;178m ▀██▄▄██▀ [38;5;32m ▀██▄▄███ [38;5;34m   ██▄▄▄ [38;5;160m  ▀██▄▄▄▄█ "
GOOGLELOGO8 = "[38;5;32m    ▀▀▀▀  [38;5;160m   ▀▀▀▀   [38;5;178m   ▀▀▀▀   [38;5;32m  ▄▀▀▀ ██ [38;5;34m    ▀▀▀▀ [38;5;160m    ▀▀▀▀▀  "
GOOGLELOGO9 = "[38;5;32m          [38;5;160m          [38;5;178m          [38;5;32m  ▀████▀▀ [38;5;34m         [38;5;160m           "
BGBb = "\033[48;5;15m \033[m"
GOOGLELOGOb = "\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;00m: \033[1C\033[48;5;252m"
BGb = "\033[48;5;252m \033[m"
SEARCHBUTTONb = "\033[m\033[48;5;252m \033[48;5;15m\033[38;5;00m SEARCH \033[m\033[48;5;252m \033[m"
BGB = "\033[48;5;252m \033[m"
GOOGLELOGO = "\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;00m: \033[1C\033[48;5;252m"
BG = "\033[48;5;15m \033[m"
SEARCHBUTTON = "\033[m\033[48;5;15m \033[48;5;252m\033[38;5;00m SEARCH \033[m\033[48;5;15m \033[m"
init = 1

def askifuse(x):
	theme = str(x)
	print("Do you want to use this theme/logo?")
	USEYN = input("[y/N]: ")
	if USEYN == 'y':
		os.system('cp -r ' + theme + '~/.DX2/bin/Google.com')
	elif USEYN == 'Y':
		os.system('cp -r ' + theme + '~/.DX2/bin/Google.com')
#	elif USEYN == 'n':
#		os.system('cp -r ' + theme + '~/.DX2/bin/Google.com')


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

PREVIEWBEG = ('\n\033[36m' + '─' * COLUMNS + '\r\033[' + str(int((COLUMNS - len(str(" PREVIEW - BEG "))) / 2)) + "C" + "\033[00;01m PREVIEW - BEG " + '\n')
PREVIEWEND = ('\n\033[36m' + '─' * COLUMNS + '\r\033[' + str(int((COLUMNS - len(str(" PREVIEW - BEG "))) / 2)) + "C" + "\033[00;01m PREVIEW - END " + '\n')

def ONE():
	print('\033c')
	print('  [1/4] (Default) ')
	if os.path.exists(DIRDATA) == False:
		if os.path.exists(FILEGOOGLECOM) == True:
			print('[00;01;38;5;190m  Currently set theme[m')
	else:
		checkcurrent(1)
	print(PREVIEWBEG)
	print('\n')
	getdefaultbrowser()
	print('\033[m' + '╭' + '─' * LID + '╮' + '\n\n' + '╰' + '─' * LID + '╯')
	print('\033[2A\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[m' + '\033[00;03;07;38;5;15m' + '\033[48;5;252m' + BARSTRING + '\033[00;07;38;5;15m' + ' ' * (BAR - len(BARSTRING)) + '\033[m ' + '│' + '\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[00;38;5;15m' + '\033[07m ')
	print('\033[m\n')
	print(PREVIEWEND)
	USE_YN = input("[00;01m Set this logo? [00;01;32m[[00;01my[00;01;32m][00;01mes | [00;01;38;5;226m[[00;01mN[00;01;38;5;226m][00;01mo | [00;01;38;5;196m[[00;01mq[00;01;38;5;196m][00;01muit: ")
#	USE_YN = input("Set this logo? [y/N]: ")
	if USE_YN == 'y':
		writefile(1)
#		os.system('cp -r ' + PWD + '/1 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'Y':
		writefile(1)
#		os.system('cp -r ' + PWD + '/1 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'N':
		TWO()
#		print("exiting ...")
	elif USE_YN == 'n':
		TWO()
#		print("exiting ...")
	elif USE_YN == '':
		TWO()
	elif USE_YN == 'q':
		print("exiting ...")
	elif USE_YN == 'Q':
		print("exiting ...")
#		print("exiting ...")
	else:
#		print("error - invalid key.")
		print("\n\033[00;01;31mError\033[m - \033[00;01;31minvalid key\033[m\n\n")


#####
def TWO():
	print('\033c')
	print('  [2/4]')
	checkcurrent(2)
	print(PREVIEWBEG)
	print("\n")
	print(" " + BG * (COLUMNS - 2) + "\n " + BG + BGB * (COLUMNS - 4) + BG + "\033[10D" + SEARCHBUTTON + "\n " + BG * (COLUMNS - 2) + "\n\r\033[2A\033[2C" + "\033[48;5;15m " + GOOGLELOGO + "\033[0m", end="")
#	searchq = input("\033[38;5;00m\033[48;5;252m")
	print("\033[m\n\n")
	print(PREVIEWEND)
	USE_YN = input("[00;01m Set this logo? [00;01;32m[[00;01my[00;01;32m][00;01mes | [00;01;38;5;226m[[00;01mN[00;01;38;5;226m][00;01mo | [00;01;38;5;196m[[00;01mq[00;01;38;5;196m][00;01muit: ")
#	USE_YN = input(" Set this logo? [y]es/[N]o/[Q]uit: ")
#	USE_YN = input("Set this logo? [y/N]: ")
	if USE_YN == 'y':
		writefile(2)
#		os.system('cp -r ' + PWD + '/2 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'Y':
		writefile(2)
#		os.system('cp -r ' + PWD + '/2 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'N':
		THREE()
#		print("exiting ...")
	elif USE_YN == 'n':
		THREE()
#		print("exiting ...")
	elif USE_YN == '':
		THREE()
	elif USE_YN == 'q':
		print("exiting ...")
	elif USE_YN == 'Q':
		print("exiting ...")
#		print("exiting ...")
	else:
		print("\n\033[00;01;31mError\033[m - \033[00;01;31minvalid key\033[m\n\n")
#		print("error - invalid key.")


def THREE():
#	print('[4/4]')
	print('\033c')
	print('  [3/4]')
	checkcurrent(3)
	print(PREVIEWBEG)
	print("\n")
	print(" " + BGb * (COLUMNS - 2) + "\n " + BGb + BGBb * (COLUMNS - 4) + BGb + "\033[10D" + SEARCHBUTTONb + "\n " + BGb * (COLUMNS - 2) + "\n\r\033[2A\033[2C" + "\033[48;5;252m " + GOOGLELOGOb + "\033[0m", end="")
	print("\033[m\n\n")
	print(PREVIEWEND)
	USE_YN = input("[00;01m Set this logo? [00;01;32m[[00;01my[00;01;32m][00;01mes | [00;01;38;5;226m[[00;01mN[00;01;38;5;226m][00;01mo | [00;01;38;5;196m[[00;01mq[00;01;38;5;196m][00;01muit: ")
#	USE_YN = input(" Set this logo? [y]es/[N]o/[Q]uit: ")
#	USE_YN = input("Set this logo? [y/N]: ")
	if USE_YN == 'y':
		writefile(3)
#		os.system('cp -r ' + PWD + '/3 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'Y':
		writefile(3)
#		os.system('cp -r ' + PWD + '/3 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'N':
		FOUR()
	elif USE_YN == 'n':
		FOUR()
#		print("exiting ...")
	elif USE_YN == '':
		FOUR()
	elif USE_YN == 'q':
		print("exiting ...")
	elif USE_YN == 'Q':
		print("exiting ...")
#		print("exiting ...")
	else:
		print("\n\033[00;01;31mError\033[m - \033[00;01;31minvalid key\033[m\n\n")
#		print("error - invalid key.")


import shutil
import os

#COLS, LINES = shutil.get_terminal_size()
CENTEREDSPACES = int((COLUMNS - 60) / 2)
#SEARCHRESULTS = int((LINES - 4) / 5.2)


def FOUR():
#	print("\033c ")
	print('\033c')
	print('  [4/4]')
	checkcurrent(4)
	print(PREVIEWBEG)
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
	print(" " * int((COLUMNS * .4) / 2) + "\033[48;5;15m \033[m" * int(COLUMNS * .6))
	print(" ")
	print(" " * int((COLUMNS - 35) / 2) + BUTTONLINEc)
#	#searchq = input("\033[3A\033[" + str(int(((COLS * .4) / 2)) + 1) + "C\033[48;5;15m\033[38;5;00m")
	print("\033[3B")
	print(PREVIEWEND)
	USE_YN = input("[00;01m Set this logo? [00;01;32m[[00;01my[00;01;32m][00;01mes | [00;01;38;5;226m[[00;01mN[00;01;38;5;226m][00;01mo | [00;01;38;5;196m[[00;01mq[00;01;38;5;196m][00;01muit: ")
#	USE_YN = input(" Set this logo? [y]es/[N]o/[Q]uit: ")
	if USE_YN == 'y':
		writefile(4)
#		os.system('cp -r ' + PWD + '/4 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'Y':
		writefile(4)
#		os.system('cp -r ' + PWD + '/4 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'N':
		ONE()
#		print("exiting ...")
	elif USE_YN == 'n':
		ONE()
#		print("exiting ...")
	elif USE_YN == '':
		ONE()
	elif USE_YN == 'q':
		print("exiting ...")
	elif USE_YN == 'Q':
		print("exiting ...")
	else:
		print("\n\033[00;01;31mError\033[m - \033[00;01;31minvalid key\033[m\n\n")
#		print("error - invalid key.")

#		os.system('cp -r ' + PWD + '/4 ' + HOME + '/.DX2/bin/Google.com')

ONE()
#os.system('dx2googler --colors BmcgxX -n ' + str(SEARCHRESULTS) + ' ' + searchq)


#######
