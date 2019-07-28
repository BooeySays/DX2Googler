#!/bin/bash

if [ "$(w3m -version | grep -qe 'w3m'; echo $?)" -eq '0' ]; then
    export BROWSER=w3m
else
    sudo apt update -y && sudo apt install w3m -y
    export BROWSER=w3m
fi


alias 'Google.com'='GooglePrompt'
if [ $BASH ]; then
    bind '"\C-k":"Google.com\n"'
elif [ $ZSH ]; then
    bindkey -s '\C-k' 'Google.com\n'
fi
