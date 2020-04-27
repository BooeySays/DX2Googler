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
					;;
				"n"|"N")
					echo -e "Exiting"
					return
					;;
				*)
					echo -e "\nInvalid key - try again"
					;;
			esac
	done
fi

sudo apt-get install w3m -y;

make;
make install;
