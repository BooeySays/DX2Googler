#!/usr/bin/env python3

import shutil
import os
import sys


PWD = os.getenv('PWD')
HOME = os.getenv('HOME')
DEFBROWSER = os.getenv("BROWSER")
BUTTONSEARCHc = "[m[38;5;00m[48;5;252m Google Search [m"		# 15 wide
BUTTONLUCKYc = "[m[38;5;00m[48;5;252m I'm Feeling Lucky [m"	# 19 wide
BUTTONLINEc = (BUTTONSEARCHc + "\033[m " + BUTTONLUCKYc)			# 35 wide
GOOGLELOGO1 = "[38;5;32m          [38;5;160m          [38;5;215m          [38;5;32m          [38;5;34m         [38;5;160m           "
GOOGLELOGO2 = "[38;5;32m    ▄▄▄▄  [38;5;160m          [38;5;215m          [38;5;32m          [38;5;34m ▄▄▄▄    [38;5;160m           "
GOOGLELOGO3 = "[38;5;32m  ██▀▀▀▀█ [38;5;160m          [38;5;215m          [38;5;32m          [38;5;34m ▀▀██    [38;5;160m           "
GOOGLELOGO4 = "[38;5;32m ██       [38;5;160m  ▄████▄  [38;5;215m  ▄████▄  [38;5;32m  ▄███▄██ [38;5;34m   ██    [38;5;160m   ▄████▄  "
GOOGLELOGO5 = "[38;5;32m ██  ▄▄▄▄ [38;5;160m ██▀  ▀██ [38;5;215m ██▀  ▀██ [38;5;32m ██▀  ▀██ [38;5;34m   ██    [38;5;160m  ██▄▄▄▄██ "
GOOGLELOGO6 = "[38;5;32m ██  ▀▀██ [38;5;160m ██    ██ [38;5;215m ██    ██ [38;5;32m ██    ██ [38;5;34m   ██    [38;5;160m  ██▀▀▀▀▀▀ "
GOOGLELOGO7 = "[38;5;32m  ██▄▄▄██ [38;5;160m ▀██▄▄██▀ [38;5;215m ▀██▄▄██▀ [38;5;32m ▀██▄▄███ [38;5;34m   ██▄▄▄ [38;5;160m  ▀██▄▄▄▄█ "
GOOGLELOGO8 = "[38;5;32m    ▀▀▀▀  [38;5;160m   ▀▀▀▀   [38;5;215m   ▀▀▀▀   [38;5;32m  ▄▀▀▀ ██ [38;5;34m    ▀▀▀▀ [38;5;160m    ▀▀▀▀▀  "
GOOGLELOGO9 = "[38;5;32m          [38;5;160m          [38;5;215m          [38;5;32m  ▀████▀▀ [38;5;34m         [38;5;160m           "
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
	print('  [1/4]')
	print(PREVIEWBEG)
	print('\n')
	getdefaultbrowser()
	print('\033[m' + '╭' + '─' * LID + '╮' + '\n\n' + '╰' + '─' * LID + '╯')
	print('\033[2A\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[m' + '\033[00;03;07;38;5;15m' + '\033[48;5;252m' + BARSTRING + '\033[00;07;38;5;15m' + ' ' * (BAR - len(BARSTRING)) + '\033[m ' + '│' + '\r' + '│' + '\033[01;38;5;32m Ｇ\033[38;5;160mｏ\033[38;5;215mｏ\033[38;5;32mｇ\033[38;5;34mｌ\033[38;5;160mｅ\033[38;5;15m：\033[00;38;5;15m' + '\033[07m ')
	print('\033[m\n')
	print(PREVIEWEND)
	USE_YN = input(" Set this logo? [y]es/[N]o/[Q]uit: ")
#	USE_YN = input("Set this logo? [y/N]: ")
	if USE_YN == 'y':
		os.system('cp -r ' + PWD + '/1 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'Y':
		os.system('cp -r ' + PWD + '/1 ' + HOME + '/.DX2/bin/Google.com')
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
	print(PREVIEWBEG)
	print("\n")
	print(" " + BG * (COLUMNS - 2) + "\n " + BG + BGB * (COLUMNS - 4) + BG + "\033[10D" + SEARCHBUTTON + "\n " + BG * (COLUMNS - 2) + "\n\r\033[2A\033[2C" + "\033[48;5;15m " + GOOGLELOGO + "\033[0m", end="")
#	searchq = input("\033[38;5;00m\033[48;5;252m")
	print("\033[m\n\n")
	print(PREVIEWEND)
	USE_YN = input(" Set this logo? [y]es/[N]o/[Q]uit: ")
#	USE_YN = input("Set this logo? [y/N]: ")
	if USE_YN == 'y':
		os.system('cp -r ' + PWD + '/2 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'Y':
		os.system('cp -r ' + PWD + '/2 ' + HOME + '/.DX2/bin/Google.com')
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
	print(PREVIEWBEG)
	print("\n")
	print(" " + BGb * (COLUMNS - 2) + "\n " + BGb + BGBb * (COLUMNS - 4) + BGb + "\033[10D" + SEARCHBUTTONb + "\n " + BGb * (COLUMNS - 2) + "\n\r\033[2A\033[2C" + "\033[48;5;252m " + GOOGLELOGOb + "\033[0m", end="")
	print("\033[m\n\n")
	print(PREVIEWEND)
	USE_YN = input(" Set this logo? [y]es/[N]o/[Q]uit: ")
#	USE_YN = input("Set this logo? [y/N]: ")
	if USE_YN == 'y':
		os.system('cp -r ' + PWD + '/3 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'Y':
		os.system('cp -r ' + PWD + '/3 ' + HOME + '/.DX2/bin/Google.com')
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
	USE_YN = input(" Set this logo? [y]es/[N]o/[Q]uit: ")
	if USE_YN == 'y':
		os.system('cp -r ' + PWD + '/4 ' + HOME + '/.DX2/bin/Google.com')
	elif USE_YN == 'Y':
		os.system('cp -r ' + PWD + '/4 ' + HOME + '/.DX2/bin/Google.com')
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
