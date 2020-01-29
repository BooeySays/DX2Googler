import os
import sys
import shutil

COLS, LINES = shutil.get_terminal_size()
dash = '─'

def titlebar(x):
	TITLE = str(x)
	print('\033c')
	print('\033[00;01;38;5;196m' + dash * COLS + '\r\033[1C\033[00;01m DX2Googler Setup - ' + TITLE + ' \033[m\n')

def menuMain():
	titlebar('Main Menu')
	print('test')

def menuHotkey():
	titlebar('Hotkey Setup')
	print("""\t\
By default, the Google search hotkey (Keyboard Shortcut) is set to:
\t\t\033[3m[CTRL] + [K]\033[23m

\tthe default search hotkey used for most web browsers""")

menuHotkey()
