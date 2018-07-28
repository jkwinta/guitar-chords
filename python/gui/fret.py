import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

REGULAR = 'regular'
LEFT_DOT = 'left_dot'
RIGHT_DOT = 'right_dot'
NUT = 'nut'

DECORATIONS = (REGULAR, LEFT_DOT, RIGHT_DOT, NUT,)


class Fret(Gtk.EventBox):
    def __init__(self, fret_number, decoration=None):
        self.fret_number = fret_number
        if decoration not in DECORATIONS:
            decoration = REGULAR
