import tkinter as tk
from guitar_chords.gui.fret import Fret
from guitar_chords.gui.fret_decoration import FretDecorator

from guitar_chords.tunings import tunings, Tuning
from guitar_chords.chords import chords
from guitar_chords.scales import scales
from guitar_chords.notes import names_to_semitones, note_name_to_index


class Fretboard(tk.Toplevel):
    def __init__(self, master, tuning_name, keyed_note_collection,
                 orientation, number_of_frets=21, number_of_strings=6):
        super().__init__(master)
        #
        self.tuning_name = None
        self.keyed_note_collection = None
        self.orientation = orientation
        self.number_of_frets = number_of_frets
        self.number_of_strings = number_of_strings
        #
        # self.tuning = Tuning(tuning_name)
        self.tuning = None
        #
        self.frets = []

        # self.orientation = orientation
        # self.number_of_frets = number_of_frets
        # self.number_of_strings = number_of_strings
        # self.tuning_name = None
        # self.tuning_notes = ()
        # self.tuning_values = ()
        # self.keyed_note_collection = keyed_note_collection
        # self.root_name = None
        # self.root_value = None
        # self.note_collection_name = None
        # self.note_collection = []
        # self.note_collection_degrees = []
        # self.note_collection_values = []
        # self.notes = set()
        #
        # self.frets = {}

        self.fretboard_frame = FretboardFrame(self)
        fret_decorator = FretDecorator(self.number_of_frets,
                                       self.number_of_strings)
        for fret_number, string_number, deco in fret_decorator:
            fret = Fret(self.fretboard_frame, deco, self.orientation)
            if self.orientation == 'V':
                fret.grid(row=fret_number, column=string_number)
            elif self.orientation == 'H':
                fret.grid(row=(self.number_of_strings - string_number - 1),
                          column=fret_number)

            self.frets.append({'fret_number': fret_number,
                               'string_number': string_number,
                               'fret': fret})
        self.fretboard_frame.pack()
        self.update_fretboard(tuning_name, keyed_note_collection)

    # def update_attributes(self):
    #     """Called after setting tuning_name, root_name, and note_collection_name
    #     to update other attributes.
    #     """
    #     self.tuning_notes = tunings[self.tuning_name]
    #     self.tuning_values = tuple(note_name_to_index(n)
    #                                for n in self.tuning_notes)
    #
    #     self.root_value = note_name_to_index(self.root_name)
    #
    #     if self.note_collection_name[0] == 'scale':
    #         self.note_collection = scales[self.note_collection_name[1]]
    #     elif self.note_collection_name[0] == 'chord':
    #         self.note_collection = chords[self.note_collection_name[1]]
    #     else:
    #         self.note_collection = []
    #
    #     self.note_collection_degrees = [
    #         int('0' + ''.join(c for c in n if c.isdigit()))
    #         for n in self.note_collection]
    #     self.note_collection_values = [
    #         names_to_semitones[n] for n in self.note_collection]
    #
    #     self.notes = {(n + self.root_value) % 12
    #                   for n in self.note_collection_values}

    def update_fretboard(self, tuning_name, keyed_note_collection):
        if (self.tuning_name, self.keyed_note_collection) == (
                tuning_name, keyed_note_collection):
            return
        # Set all attr declared in init:
        self.keyed_note_collection = keyed_note_collection
        self.tuning_name = tuning_name
        self.tuning = Tuning(tuning_name)

        for fret_content in self.frets:
            fret_number = fret_content['fret_number']
            string_number = fret_content['string_number']
            fret = fret_content['fret']
            note_value = self.tuning.get_fret_note(string_number, fret_number)
            if self.keyed_note_collection.contains_note_value(note_value):
                fret.set_fretted()
            else:
                fret.set_unfretted()

    # def set_fretting(self):
    #     pass  # TODO

    def clear_fretboard(self):
        for fret_content in self.frets:
            fret_content['fret'].set_unfretted()


class FretboardFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
