#!/bin/bash

if [ -f "$HOME/.dx2rc" ]; then
	echo -en """
.dx2rc has already been copied to \$HOME.

[ Hit any key to continue ]

"""
	read
else
	cp ./.dx2rc "$HOME/"
	echo -en """
.dx2rc has been copied.

[ Hit any key to continue ]

"""
	read
fi


clear
echo -en """\033c

Modifying ~/.bashrc to source .dx2rc.


[ Hit any key to continue ]

"""
read
echo -en """
### BEG - SOURCE DX2RC ###
if [ -f "$HOME/.dx2rc" ]; then
	source "$HOME/.dx2rc";
fi
### END - SOURCE DX2RC ###
""" >> ~/.bashrc
echo -en """

.bashrc has been edited.


[ Hit any key to continue ]

"""
read
