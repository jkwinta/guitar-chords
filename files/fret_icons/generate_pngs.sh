#!/bin/bash

# WIDTH=24
# HEIGHT=36
#WIDTH=32
#HEIGHT=40
WIDTH=28
HEIGHT=35

for file in *.svg
do
    inkscape -z $PWD/$file -e  $PWD/png/${file/%.svg/.png} -w $WIDTH -h $HEIGHT -b "#ffffff"
done
