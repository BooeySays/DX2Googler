#!/usr/bin/env python3

import os

DEFBROWSER = os.getenv("BROWSER")

def getdefaultbrowser():
	defbrowserprompt = "\033[00;01;38;5;51mDefault Browser\033[00;01m: "
	if os.getenv("aBROWSER") is None:
		DEFBROW = "\033[00;01;38;5;196mERR\033[00;01m - Default browser is not set"
	else:
		DEFBROW = str.upper(os.getenv("BROWSER"))
	print(defbrowserprompt + DEFBROW)

getdefaultbrowser()
