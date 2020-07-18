import sys
import os
import shutil

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
	[3] Updates

"""
	checkforupdates = """  Choose option to configure:

	[1] Check for updates
	[2] Download / Install newest update

"""
	bottomoptions = """
	[M]ain Menu
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
		print(menutext.bottomoptions)
		selection = input("\n : ")
		if selection == "1":
			print(options[int(selection)])
		elif selection == "2":
			print("selection 2")
		elif selection == "m":
			menus.mainmenu()
		elif selection == "M":
			menus.mainmenu()
	def googlescreen():
#		options = {1:"Check for updates", 2:"Download and install newest update"}
		tools.titlebar()
		print(menutext.checkforupdates)
		print(menutext.updatequit)
		selection = input("\n : ")
		if selection == "1":
			print(options[int(selection)])
		elif selection == "2":
			print(options[int(selection)])
#			print("selection 2")


menus.mainmenu()