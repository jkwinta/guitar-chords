from python.gui.fretboard_decoration import StandardFretboardDecoration
from python.gui.fret import Fret

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

DEFAULT_STRINGS = 6
DEFAULT_FRETS = 21


class Fretboard(Gtk.Window):
    def __init__(self, fretboard_decoration):
        Gtk.Window.__init__(self)
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.frets = [[] for _ in range(DEFAULT_STRINGS)]
        for i in range(DEFAULT_STRINGS):
            for j in range(DEFAULT_FRETS + 1):
                new_fret = Fret(j, fretboard_decoration.get_at(i, j))
                self.frets[i].append(new_fret)
                self.grid.attach(new_fret, i, j, 1, 1)


if __name__ == '__main__':
    g = Fretboard(StandardFretboardDecoration)
    g.connect("destroy", Gtk.main_quit)
    g.show_all()
    Gtk.main()
    print(end='')
