import os, sys
import shutil

COLS, LINES = shutil.get_terminal_size()

selectedmodkey = None
CTRL = '[38;5;196m[[00;01mCTRL[38;5;196m][m'
ALT = '[38;5;196m[[00;01mALT[38;5;196m][m'
CTRLALT = '[38;5;196m[[00;01mCTRL[38;5;196m][00;01m + [38;5;196m[[00;01mALT[38;5;196m][m'
hotkey = 'k'
HOTKEY = ('[38;5;196m[[00;01m' + hotkey + '[38;5;196m][m')
FINALMOD = CTRL
FINALHOTKEY = (FINALMOD + ' + ' + HOTKEY)

options = """	[1]	Edit Modifier key (""" + CTRL + """/""" + ALT + """/""" + CTRLALT + """)
	[2]	Edit Hot key (Currently: """ + HOTKEY + """)"""


def previewhotkey():
	print('c' + '[48;5;21m' + ' ' * COLS + '\r  HOTKEY PREVIEW:' + '[m\n')
	print('\t\tMOD KEY\t:\t' + FINALMOD)
	print('\t\tHOT KEY\t:\t' + HOTKEY)
	print('\n')
	print('\t\tSequence:\t', end='')
	print(FINALHOTKEY + '\n\n')
	print(options)
#	print(' ' * int((COLS - 12) / 2) + FINALHOTKEY)

def selectmodkey():
	FINALMOD = CTRL
	print('c' + '[48;5;21m' + ' ' * COLS + '\r  SELECT MODIFIER KEY:' + '[m\n')
	print('\n\t\tCurrent Modifier Key\t:\t' + FINALMOD + '')
	print('\n\t[1]	CTRL\n\t[2]	ALT\n\t[3]	CTRL + ALT\n\n')
	selectedmodkey = input(": ")
	if selectedmodkey == '1':
		FINALMOD = CTRL
	elif selectedmodkey == '2':
		FINALMOD = ALT
	elif selectedmodkey == '3':
		FINALMOD = CTRLALT
	else:
		print('err - invalid key')
	print(FINALMOD)

#previewhotkey()
selectmodkey()


#[
