#!/usr/bin/env bash

if [ ! -d "$HOME/.DX2" ]; then
	while true; do
		echo -e "DX2Googler requires SetupDX2"
		echo -e "Install it now?"
		echo -e ""
		read -p "[Y/n]: "
			case $REPLY in
				""|"y"|"Y")
					sudo apt-get update -y
					sudo apt-get install w3m make python3 wget -y
					wget https://raw.githubusercontent.com/BooeySays/SetupDx2/master/Setup.py
					read -p "[ Hit any key to set up DX2 ]" -n 1;
					python3 ./Setup.py
					echo -e "\nDONE !!\n"
					if ! command -v w3m &> /dev/null; then
						echo -e "w3m not found";
						sudo apt-get update -y;
						sudo apt-get install w3m -y;
					fi
					if ! command -v make &> /dev/null; then
						echo -e "Make not found"
						sudo apt-get update -y;
						sudo apt-get install make -y;
					fi
					if ! command -v python3 &> /dev/null; then
						echo -e "Python3 not found"
						sudo apt-get update -y;
						sudo apt-get install python3 -y;
					fi
				#	echo -e "\033[m\033[01;31mInstalling w3m and make\033[m:";
				#	sudo apt-get install w3m make -y;
					read -p "[m[01;31mFinished - Press any key to continue and install dx2googler" -n 1;
					make;
#					make
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
	if ! command -v w3m &> /dev/null; then
		echo -e "w3m not found";
		sudo apt-get update -y;
		sudo apt-get install w3m -y;
	fi
	if ! command -v make &> /dev/null; then
		echo -e "Make not found"
		sudo apt-get update -y;
		sudo apt-get install make -y;
	fi
	if ! command -v python3 &> /dev/null; then
		echo -e "Python3 not found"
		sudo apt-get update -y;
		sudo apt-get install python3 -y;
	fi
#	echo -e "\033[m\033[01;31mInstalling w3m and make\033[m:";
#	sudo apt-get install w3m make -y;
	read -p "[m[01;31mFinished - Press any key to continue and install dx2googler[m" -n 1;
	make;
fi

