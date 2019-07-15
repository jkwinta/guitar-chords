#!/bin/bash

# WIDTH=24
WIDTH=32
# HEIGHT=36
HEIGHT=40

for file in *.svg
do
    inkscape -z $PWD/$file -e  $PWD/png/${file/%.svg/.png} -w $WIDTH -h $HEIGHT -b "#ffffff"
done
