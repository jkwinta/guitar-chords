import tkinter as tk

from files.fret_icons.generate_colour_svgs import get_colours as get_svg_colours
from guitar_chords.gui.fret import Fret


class Legend(tk.Frame):

    def __init__(self, master, keyed_note_collection, preferred_colours=None):
        super().__init__(master)
        self.keyed_note_collection = keyed_note_collection
        self.all_colours = None
        self.colours = None
        self.colour_map = None
        if preferred_colours is None:
            self.preferred_colours = []
        else:
            self.preferred_colours = preferred_colours

        self.frets = []
        self.description_labels = []

        self.build_gui()

    def get_colours(self):
        if self.colours is None:
            all_colours = get_svg_colours()
            valid_prefered_colours = [colour for colour in
                                      self.preferred_colours
                                      if colour in all_colours]
            remaining_colours = [colour for colour in all_colours
                                 if colour not in valid_prefered_colours]
            colour_order = valid_prefered_colours + remaining_colours
            self.colours = colour_order[:len(self.keyed_note_collection)]
        return self.colours

    def get_colour_map(self):
        if self.colour_map is None:
            self.colour_map = {value: colour for value, colour in
                               zip(self.keyed_note_collection.get_note_values(),
                                   self.get_colours())}
        return self.colour_map

    def get_note_colour(self, note_value):
        return self.get_colour_map().get(note_value % 12)

    def build_gui(self):
        i = 0
        for colour, note in zip(self.get_colours(),
                                self.keyed_note_collection.notes):
            fret = Fret(self)
            fret.grid(row=i, column=0)
            fret.set_fretted(colour.lower())
            self.frets.append(fret)
            desc_label = tk.Label(self,
                                  text='{} ({})'.format(note.degree, note.name),
                                  anchor=tk.W, justify=tk.LEFT)
            desc_label.grid(row=i, column=1)
            self.description_labels.append(desc_label)
            i += 1

# class LegendToplevel(tk.Toplevel):
#
#     def __init__(self, master, notes, preferred_colours=None):
#         super().__init__(master)
#         self.legend_frame = Legend(self, notes, preferred_colours)
#         self.legend_frame.pack()
#
#     def get_colour_map(self):
#         return self.legend_frame.get_colour_map()
