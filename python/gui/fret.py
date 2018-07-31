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


# PIXBUFS = {k: tuple(GdkPixbuf.Pixbuf.new_from_file(p) for p in v) for k, v in ICON_PATHS.items()}


class Fret(Gtk.EventBox):
    def __init__(self, fret_number, decoration=None):
        Gtk.EventBox.__init__(self)
        self.fret_number = fret_number
        if decoration not in DECORATIONS:
            decoration = REGULAR
        self.standard_image, self.fretted_image = (Gtk.Image.new_from_file(p) for p in ICON_PATHS[decoration])
        # self.standard_image, self.fretted_image = (Gtk.Image.new_from_pixbuf(pb) for pb in PIXBUFS[decoration])
        self.add(self.standard_image)

    def set(self):
        self.add(self.fretted_image)

    def unset(self):
        self.add(self.standard_image)
