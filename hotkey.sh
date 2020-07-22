#export BROWSER=w3m
MODIFIERKEYA='\C-'
MODIFIERKEYB='j'


echo  """if [ \$BASH ]; then
    bind '\"$MODIFIERKEYA$MODIFIERKEYB\":\"Google.com\\n\"'
elif [ \$ZSH ]; then
    bindkey -s '$MODIFIERKEYA$MODIFIERKEYB' 'Google.com\\n'
fi""" > ./hotkey.rc
