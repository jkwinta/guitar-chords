import os
import pathlib
from xml.etree import ElementTree

INITIAL_COLOUR = '0000FF'


def get_colours():
    colour_file = pathlib.Path(__file__).parent / 'colours'
    colours = {}
    with open(colour_file) as f:
        lines = f.readlines()
        for line in lines:
            if line:
                colour_name, colour_hex_value = line.split(':')
                colours[colour_name.strip()] = colour_hex_value.strip()
    return colours


svg_directory = pathlib.Path(__file__).parent / 'svg'


def get_svg_files():
    for svg_file in os.listdir(svg_directory):
        if svg_file.endswith('.svg'):
            yield svg_directory / svg_file


def is_blue_circle(element):
    return element.tag.endswith('circle') and \
           'fill:#0000ff' in element.attrib.get('style', '').lower().split(';')


def change_element_fill_colour(element, new_colour):
    style_items = [si for si in element.attrib.get('style', '').split(';')
                   if si and si.split(':')[0] != 'fill']
    style_items = ['fill:#{}'.format(new_colour.lower())] + style_items
    element.set('style', ';'.join(style_items))


if __name__ == '__main__':
    colour_map = get_colours()
    for svg_file in get_svg_files():
        print(svg_file)
        element_tree = ElementTree.parse(svg_file)
        blue_circles = [element for element in element_tree.getiterator() if is_blue_circle(element)]
        if blue_circles:
            for colour_name, colour_hex_value in colour_map.items():
                for element in blue_circles:
                    change_element_fill_colour(element, colour_hex_value)
                colour_dir = svg_directory / colour_name.lower()
                if not os.path.exists(colour_dir):
                    os.makedirs(colour_dir)
                element_tree.write(colour_dir / svg_file.name)
