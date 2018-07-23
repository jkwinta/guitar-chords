#!/usr/bin/bash

WIDTH=32
HEIGHT=32

for file in *.svg
do
    # echo $file  png/${file/%.svg/.png}
    inkscape -z $file -e  png/${file/%.svg/.png} -w $WIDTH -h $HEIGHT
done
