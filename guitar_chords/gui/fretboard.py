import tkinter as tk
from .fret import Fret
from .fret_decoration import FretDecorator

from ..tunings import tunings
from ..chords import chords
from ..scales import scales
from ..notes import names_to_semitones, note_name_to_index


class Fretboard(tk.Toplevel):
    def __init__(self, master, tuning, root, note_collection,
                 orientation='V', number_of_frets=21, number_of_strings=6):
        super().__init__(master)
        self.orientation = orientation
        self.number_of_frets = number_of_frets
        self.number_of_strings = number_of_strings
        self.tuning_name = None
        self.tuning_notes = ()
        self.tuning_values = ()
        self.root_name = None
        self.root_value = None
        self.note_collection_name = None
        self.note_collection = []
        self.note_collection_degrees = []
        self.note_collection_values = []
        self.notes = set()

        self.frets = {}
        self.fretboard_frame = FretboardFrame(self)
        for fret_number, string_number, deco in FretDecorator(
                self.number_of_frets, self.number_of_strings):
            fret = Fret(self.fretboard_frame, deco, self.orientation)
            if self.orientation == 'V':
                fret.grid(row=fret_number, column=string_number)
            elif self.orientation == 'H':
                fret.grid(row=(self.number_of_strings - string_number - 1),
                          column=fret_number)

            self.frets[fret_number, string_number] = fret
        self.fretboard_frame.pack()
        self.update_fretboard(tuning, root, note_collection)

    def update_attributes(self):
        """Called after setting tuning_name, root_name, and note_collection_name
        to update other attributes.
        """
        self.tuning_notes = tunings[self.tuning_name]
        self.tuning_values = tuple(note_name_to_index(n)
                                   for n in self.tuning_notes)

        self.root_value = note_name_to_index(self.root_name)

        if self.note_collection_name[0] == 'scale':
            self.note_collection = scales[self.note_collection_name[1]]
        elif self.note_collection_name[0] == 'chord':
            self.note_collection = chords[self.note_collection_name[1]]
        else:
            self.note_collection = []

        self.note_collection_degrees = [
            int('0' + ''.join(c for c in n if c.isdigit()))
            for n in self.note_collection]
        self.note_collection_values = [
            names_to_semitones[n] for n in self.note_collection]

        self.notes = {(n + self.root_value) % 12
                      for n in self.note_collection_values}

    def update_fretboard(self, tuning, root, note_collection):
        if (self.tuning_name, self.root_name, self.note_collection_name) == (
                tuning, root, note_collection):
            return
        # Set all attr declared in init:
        self.tuning_name = tuning
        self.root_name = root
        self.note_collection_name = note_collection

        self.update_attributes()

        for ix, fret in self.frets.items():
            fret_number, string_number = ix
            fret_value = self.tuning_values[string_number] + fret_number
            if fret_value % 12 in self.notes:
                fret.set_fretted()
            else:
                fret.set_unfretted()

    def clear_fretboard(self):
        # TODO
        pass


class FretboardFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
