import sys, os, shutil

COLS, LINES = shutil.get_terminal_size()
_VERSION_ = "0.1"
_TITLE_ = "DX2Googler Configuration"

class tools:
	def titlebar():
		print("\033c\033[48;5;21m" + " " * COLS + "\r  " + str(_TITLE_) + " v" + str(_VERSION_) + "\033[m\n")

class menutext:
	main = """  Choose option to configure:

	[1] Google search screen
	[2] Hotkey



	[C]heck for updates
	[U]ninstall
	[Q]uit
"""
	update = """
	update
"""

class menus:
	def mainmenu():
		options = {1:"Google search screen", 2:"Hotkeys"}
		tools.titlebar()
		print(menutext.main)
		selection = input("\n\n : ")
		if selection == "1":
			print(options[int(selection)])
		elif selection == "2":
			print("selection 2")


menus.mainmenu()