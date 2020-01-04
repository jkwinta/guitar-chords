#!/bin/bash

# WIDTH=24
# HEIGHT=36
#WIDTH=32
#HEIGHT=40
WIDTH=28
HEIGHT=35

for file in $(find $PWD/svg | grep -v unused)
do
  echo $file
  if [ -d $file ]
   then
     echo 'dir'
    else
      echo ${file//svg/gif}
#      inkscape -z $file -e  ${file/%.svg/.png} -w $WIDTH -h $HEIGHT -b "#ffffff"
  fi
#  echo $file
#  echo ${file/%.svg/.gif}
#    inkscape -z $PWD/$file -e  $PWD/png/${file/%.svg/.png} -w $WIDTH -h $HEIGHT -b "#ffffff"
done
