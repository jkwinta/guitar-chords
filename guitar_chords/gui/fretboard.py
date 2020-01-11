import tkinter as tk
from guitar_chords.gui.fret import Fret
from guitar_chords.gui.fret_decoration import FretDecorator
from guitar_chords.gui.legend import Legend

from guitar_chords.tunings import tunings, Tuning
from guitar_chords.chords import chords
from guitar_chords.scales import scales
from guitar_chords.notes import names_to_semitones, note_name_to_index


class Fretboard(tk.Frame):

    def __init__(self, master, orientation, number_of_frets=21,
                 number_of_strings=6, legend=True):
        super().__init__(master)
        #
        self.keyed_note_collection = None
        self.tuning_name = None
        self.tuning = None
        self.orientation = orientation
        self.number_of_frets = number_of_frets
        self.number_of_strings = number_of_strings
        self.legend_arg = legend
        self.legend = None

        self.frets = []

        fret_decorator = FretDecorator(self.number_of_frets,
                                       self.number_of_strings)
        for fret_number, string_number, deco in fret_decorator:
            fret = Fret(self, deco, self.orientation)
            if self.orientation == 'V':
                fret.grid(row=fret_number, column=string_number)
            elif self.orientation == 'H':
                fret.grid(row=(self.number_of_strings - string_number - 1),
                          column=fret_number)

            self.frets.append({'fret_number': fret_number,
                               'string_number': string_number,
                               'fret': fret})

    def update_fretboard(self, tuning_name, keyed_note_collection):
        if (self.tuning_name, self.keyed_note_collection) == (
                tuning_name, keyed_note_collection):
            return
        # Set all attr declared in init:
        self.keyed_note_collection = keyed_note_collection
        self.tuning_name = tuning_name
        self.tuning = Tuning(tuning_name)

        if self.legend_arg:
            self.legend = Legend(self, self.keyed_note_collection)

        for fret_content in self.frets:
            fret_number = fret_content['fret_number']
            string_number = fret_content['string_number']
            fret = fret_content['fret']
            note_value = self.tuning.get_fret_note(string_number, fret_number)
            if self.keyed_note_collection.contains_note_value(note_value):
                fret.set_fretted()
            else:
                fret.set_unfretted()

    def clear_fretboard(self):
        for fret_content in self.frets:
            fret_content['fret'].set_unfretted()

    def get_orientation(self):
        return self.orientation

    def get_legend(self):
        return self.legend


class FretboardToplevel(tk.Toplevel):

    def __init__(self, master, orientation, number_of_frets=21,
                 number_of_strings=6, legend=False):
        super().__init__(master)
        self.fretboard_frame = Fretboard(self, orientation,
                                         number_of_frets, number_of_strings,
                                         legend)
        self.fretboard_frame.pack()

    def update_fretboard(self, tuning_name, keyed_note_collection):
        self.title(str(keyed_note_collection))
        self.fretboard_frame.update_fretboard(tuning_name, keyed_note_collection
                                              )

    def clear_fretboard(self):
        self.fretboard_frame.clear_fretboard()

    def get_orientation(self):
        return self.fretboard_frame.get_orientation()

    def get_legend(self):
        return self.fretboard_frame.get_legend()
