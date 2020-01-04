import os
import pathlib
import subprocess

# WIDTH=24
# HEIGHT=36
WIDTH=32
HEIGHT=40
# WIDTH = 28
# HEIGHT = 35

svg_directory = pathlib.Path(__file__).parent / 'svg'
gif_directory = svg_directory.parent / 'gif'


def get_source_dest_paths():
    for path in svg_directory.rglob('*'):
        relative_path = path.relative_to(svg_directory)
        if 'unused' not in relative_path.parts:
            if path.is_dir():
                (gif_directory / relative_path).mkdir(exist_ok=True)
            elif path.is_file():
                if path.name.endswith('.svg'):
                    dest_file = os.path.join(gif_directory / relative_path.parent, relative_path.name[:-4] + '.gif')
                    yield path, dest_file


def get_command_list(source_file, dest_file):
    result = ['inkscape', '-z', source_file, '-e', dest_file, '-w', str (WIDTH), '-h', str(HEIGHT), '-b' '#ffffff']
    return result

if __name__ == '__main__':
    for source, dest in get_source_dest_paths():
        print(source, dest)
        command = get_command_list(source, dest)
        print(command)
        subprocess.call(command)

#
# for file in $(find $PWD/svg | grep -v unused)
# do
#   echo $file
#   if [ -d $file ]
#    then
#      echo 'dir'
#     else
#       echo ${file//svg/gif}
# #      inkscape -z $file -e  ${file/%.svg/.png} -w $WIDTH -h $HEIGHT -b "#ffffff"
#   fi
# #  echo $file
# #  echo ${file/%.svg/.gif}
# #    inkscape -z $PWD/$file -e  $PWD/png/${file/%.svg/.png} -w $WIDTH -h $HEIGHT -b "#ffffff"
# done
