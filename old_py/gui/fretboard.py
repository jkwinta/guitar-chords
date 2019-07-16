from python.gui.fretboard_decoration import StandardFretboardDecoration
from python.gui.fret import Fret

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

DEFAULT_STRINGS = 6
DEFAULT_FRETS = 18
# DEFAULT_FRETS = 21


class Fretboard(Gtk.Window):
    def __init__(self, fretboard_decoration):
        Gtk.Window.__init__(self)
        self.fretboard_decoration = fretboard_decoration
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.frets = [[] for _ in range(DEFAULT_STRINGS)]
        for i in range(DEFAULT_STRINGS):
            for j in range(DEFAULT_FRETS + 1):
                new_fret = Fret(j, fretboard_decoration.get_at(i, j))
                self.frets[i].append(new_fret)
                self.grid.attach(new_fret, i, j, 1, 1)

    def display(self, tuning, root, chord_or_scale_set):
        notes = set((n + root) % 12 for n in chord_or_scale_set)
        for i in range(len(self.frets)):
            for j in range(len(self.frets[i])):
                if (tuning[i] + j) % 12 in notes:
                    self.frets[i][j].set()
                else:
                    self.frets[i][j].unset()


if __name__ == '__main__':
    g = Fretboard(StandardFretboardDecoration)
    g.connect("destroy", Gtk.main_quit)
    g.show_all()

    from python.tunings import STANDARD
    from python.chords import MAJOR, MINOR

    # g.display(STANDARD, 0, MAJOR)
    g.display(STANDARD, 0, MINOR)

    Gtk.main()
    print(end='')
