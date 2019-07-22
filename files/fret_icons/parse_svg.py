from xml.etree import ElementTree

et = ElementTree.parse('./left_fretted.svg')

circles = [e for e in et.getiterator() if e.tag.endswith('circle')]
blue = [e for e in et.getiterator()
        if 'fill:#0000ff' in e.attrib.get('style', '').split(';')]

print('')
