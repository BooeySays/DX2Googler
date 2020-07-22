import os, sys

CTRL = "\C-"
ALT = "\e"
CTRLALT = "\e\C-"

MODKEYA = "\C-"
MODKEYB = "k"

class keys:
	ctrl = {'key':'[CTRL]', 'code':'\C-'}
	alt = {'key':'[ALT]', 'code':'\e'}
	ctrlandalt = {'key':'[CTRL] + [ALT]', 'code':'\C-\e'}


def asktousedefault(x,y):
	MODKEYA = x
	MODKEYB = y
	print("Would you like to use the default hotkey ([CTRL] + [k]) to start a Google search from anywhere in a Terminal?")
	USEDEFAULTHOTKEYSYN = input("[Y/n]: ")
	if USEDEFAULYHOTKEYSYN == "Y":
		sethotkey()
	elif USEDEFAULYHOTKEYSYN == "y":
		sethotkey()
	elif USEDEFAULYHOTKEYSYN == "":
		sethotkey()
	elif USEDEFAULYHOTKEYSYN == "n":
		print("exiting ...")
	elif USEDEFAULYHOTKEYSYN == "N":
		print("exiting ...")
	else:
		print("Error")
	print(MODKEYA + MODKEYB)

print(keys.ctrlandalt['key'])
asktousedefault(CTRL, "k")