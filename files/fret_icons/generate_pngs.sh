#!/bin/bash

WIDTH=24
# WIDTH=32
HEIGHT=32
# HEIGHT=40

for file in *.svg
do
    # echo $file  png/${file/%.svg/.png}
    inkscape -z $PWD/$file -e  $PWD/png/${file/%.svg/.png} -w $WIDTH -h $HEIGHT
done
