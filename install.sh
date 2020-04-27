#!/usr/bin/env bash

if [ ! -d "$HOME/.DX2" ]; then
	while true; do
		echo -e "DX2Googler requires SetupDX2"
		echo -e "Install it now?"
		echo -e ""
		read -p "[Y/n]: "
			case $REPLY in
				""|"y"|"Y")
					sudo apt-get install git python3 -y
					git clone https://github.com/BooeySays/SetupDX2.git
					cd SetupDX2
					python3 ./Setup.py
					cd ..
					make
					return
					;;
				"n"|"N")
					echo -e "\nExiting"
					return
					;;
				*)
					echo -e "\n\n\033[00;01;31mERR\033[37m:\033[m Invalid key"
					echo -e ""
					echo -e "[ Press any key to try again ]"
					read -n 1
					;;
			esac
	done
else
	sudo apt-get install w3m -y;
	make;
fi
