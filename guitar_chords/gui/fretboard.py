import tkinter as tk
from .fret import Fret
from .fret_decoration import FretDecorator


class Fretboard(tk.Toplevel):
    def __init__(self, master, tuning, root, note_collection):
        super().__init__(master)
        self.tuning = tuning
        self.root = root
        self.note_collection = note_collection

        self.fretboard_frame = FretboardFrame(self)
        for fret_number, string_number, deco in FretDecorator(6, 19):
            fret = Fret(self.fretboard_frame, deco)
            fret.grid(row=fret_number, column=string_number)
        self.fretboard_frame.pack()

    def update_fretboard(self, tuning, root, note_collection):
        pass


class FretboardFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
