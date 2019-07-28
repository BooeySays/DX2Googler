#!/bin/bash

SCDIR=$PWD

# install pre-req apps:
if [ "$(w3m -version | grep -qe 'w3m'; echo $?)" != '0' ]; then
    if [ "$(wget --version | grep -qe 'wget'; echo $?)" != '0' ]; then
        sudo apt update -y && sudo apt install wget -y
    fi
    sudo apt update -y && sudo apt install w3m -y
fi

function _prepdx2(){
    wget https://raw.githubusercontent.com/BooeySays/SetupDx2/master/DX2Setup.sh
    . ./DX2Setup.sh
}

if [ ! $DX2 ] || [ ! $DX2RC ] || [ ! $DX2BIN ]; then
    _prepdx2;
fi
unset _prepdx2

cd "$SCDIR"
sudo make install;
unset SCDIR