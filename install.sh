#!/usr/bin/env bash

function checkapps(){
declare -a APPSTOCHECKFOR=("w3m" "python3" "wget" "make")

if $(! command -v w3m &> /dev/null) || $(! command -v python3 &> /dev/null) || $(! command -v wget &> /dev/null) || $(! command -v make &> /dev/null); then
	echo -e "\033[00;01;31mOne or more required apps is missing \033[m- \033[00;01;31mInstalling missing apps\033[m: "
	echo -e "In order to install the missing apps, root permission will be required / used when executing apt-get."
	echo -e "If prompted, please enter your password in the following prompt to continue.\n"
	sudo echo "";
	echo -e -n "\033[00;01;36mupdating apt-get repo\033[m\t: "
	sudo apt-get update -y &> /dev/null;
	echo -e "\033[00;01;32mDONE\033[m\n"
	for apps in ${APPSTOCHECKFOR[@]}; do
		echo -e -n "\033[00;01;36mSearching for \033[00;01m$apps\033[m\t: ";
		if ! command -v "$apps" &> /dev/null; then
			echo -e "\033[00;01;31mNot Found\033[m";
			echo -e -n "  \033[00;01m- \033[m\033[00;01;36mInstalling \033[00;01m$apps\033[m\t: ";
			sudo apt-get install "$apps" -y &> /dev/null;
			echo -e "\033[00;01;32mDONE\033[m"
		else
			echo -e "\033[00;01;32mFound\033[m"
		fi
	done
else
	echo -e "\033[00;01;32mAll required apps found\033[m"
fi
}

function installdx2setup(){
	echo -e "\033[00;01;31mSetting up DX2Setup\033[m:"
	echo -e -n "\tDownloading setup file\t: "
	wget https://raw.githubusercontent.com/BooeySays/SetupDx2/Release/Setup.py &> /dev/null;
	echo -e "\033[00;01;32mDONE\033[m"
	echo -e -n "\tSetting up DX2Setup\t: "
	python3 ./Setup.py &> /dev/null;
	echo -e "\033[00;01;32mDONE\033[m\n"
}


if [ ! -d "$HOME/.DX2" ]; then
	echo -e "DX2Googler requires SetupDX2"
	echo -e "Install it now?"
	echo -e ""
	read -p "[Y/n]: "
	case $REPLY in
		""|"y"|"Y")
			checkapps;
			installdx2setup;
			echo -e -n "\033[00;01;31mInstalling dx2googler[m\t: ";
			make &> /dev/null;
			echo -e "\033[00;01;32mDONE\033[m\n"
			. ~/.dx2rc;
			echo -e "[m[31mFINISHED[m! To start google search, hit [31m[[mCTRL[31m][m + [31m[[mk[31m][m\n";
#			read -p "[m[01;31mFinished - Press any key to continue and install dx2googler" -n 1;
#			make &> /dev/null;
#			. ~/.dx2rc;
#			echo -e "[m[31m FINISHED! To start google search, hit [CTRL] + [k]";
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
else
	checkapps;
	echo -e -n "\033[00;01;31mInstalling dx2googler[m\t: ";
	make &> /dev/null;
	echo -e "\033[00;01;32mDONE\033[m\n"
	. ~/.dx2rc;
	echo -e "[m[31mFINISHED[m! To start google search, hit [31m[[mCTRL[31m][m + [31m[[mk[31m][m\n";
#	echo -e "[m[31mFINISHED! To start google search, hit [CTRL] + [k]";
fi
