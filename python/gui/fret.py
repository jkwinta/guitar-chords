import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

REGULAR = 'regular'
LEFT_DOT = 'left_dot'
RIGHT_DOT = 'right_dot'
NUT = 'nut'

DECORATIONS = (REGULAR, LEFT_DOT, RIGHT_DOT, NUT,)

ICON_PATHS = {REGULAR: ('../../files/fret_icons/png/reg.png', '../../files/fret_icons/png/reg_fretted.png'),
              LEFT_DOT: ('../../files/fret_icons/png/left.png', '../../files/fret_icons/png/left_fretted.png'),
              RIGHT_DOT: ('../../files/fret_icons/png/right.png', '../../files/fret_icons/png/right_fretted.png'),
              NUT: ('../../files/fret_icons/png/bar.png', '../../files/fret_icons/png/bar_fretted.png'), }

ICON_IMAGES = {k: tuple(Gtk.Image.new_from_file(p) for p in v) for k, v in ICON_PATHS.items()}


# PIXBUFS = {k: tuple(GdkPixbuf.Pixbuf.new_from_file(p) for p in v) for k, v in ICON_PATHS.items()}


class Fret(Gtk.EventBox):
    def __init__(self, fret_number, decoration=None):
        self.fret_number = fret_number
        if decoration not in DECORATIONS:
            decoration = REGULAR
        self.standard_image, self.fretted_image = ICON_IMAGES[decoration]
        # self.standard_image, self.fretted_image = (Gtk.Image.new_from_pixbuf(pb) for pb in PIXBUFS[decoration])
        self.add(self.standard_image)
