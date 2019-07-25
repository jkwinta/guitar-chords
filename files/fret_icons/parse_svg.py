import os
from xml.etree import ElementTree

et = ElementTree.parse('./left_fretted.svg')

circles = [e for e in et.getiterator() if e.tag.endswith('circle')]
blue = [e for e in et.getiterator()
        if 'fill:#0000ff' in e.attrib.get('style', '').split(';')]


def are_concentric(element_1, element_2):
    centre_1 = element_1.attrib.get('cx'), element_1.attrib.get('cy')
    centre_2 = element_2.attrib.get('cx'), element_2.attrib.get('cy')
    return centre_1 == centre_2


def is_blue_circle(element):
    e_tag = element.tag
    if isinstance(e_tag, str):
        if e_tag.endswith('circle'):
            if 'fill:#0000ff' in element.attrib.get('style', '').split(';'):
                return True
    return False


for file_name in os.listdir('.'):
    if file_name.endswith('.svg'):
        # Skip bar files
        if file_name.startswith('bar'):
            continue
        et = ElementTree.parse(os.path.join('.', file_name))
        blue_circles = [e for e in et.getiterator() if is_blue_circle(e)]
        if blue_circles:
            for bc in blue_circles:
                bc.attrib['r'] = str(8)
            et.write(os.path.join('.', file_name.replace('.svg', '_smbc.svg')))

print('')
