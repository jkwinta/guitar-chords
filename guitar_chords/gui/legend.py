import tkinter as tk

from files.fret_icons.generate_colour_svgs import get_colours


class Legend(tk.Frame):

    def __init__(self, master, notes, preferred_colours=None):
        super().__init__(master)
        self.notes = notes
        self.all_colours = None
        self.colour_map = None
        if preferred_colours is None:
            self.preferred_colours = []
        else:
            self.preferred_colours = preferred_colours

    def get_colour_map(self):
        if self.colour_map is None:
            colour_order = [colour for colour in self.preferred_colours
                            if colour in get_colours()] + [
                               colour for colour in get_colours()
                               if colour not in self.preferred_colours]
            self.colour_map = {note: colour for note, colour in
                               zip(self.notes, colour_order)}
        return self.colour_map


class LegendToplevel(tk.Toplevel):

    def __init__(self, master, notes, preferred_colours=None):
        super().__init__(master)
        self.legend_frame = Legend(self, notes, preferred_colours)
        self.legend_frame.pack()

    def get_colour_map(self):
        return self.legend_frame.get_colour_map()
