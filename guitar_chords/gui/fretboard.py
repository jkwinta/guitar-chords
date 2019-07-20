import tkinter as tk
from .fret import Fret


class Fretboard(tk.Toplevel):
    def __init__(self, master, tuning, root, note_collection):
        super().__init__(master)
        self.tuning = tuning
        self.root = root
        self.note_collection = note_collection

        self.fretboard_frame = FretboardFrame(self)
        for i in range(22):
            for j in range(6):
                fret = Fret(self.fretboard_frame, '')
                fret.grid(row=i, column=j)
        self.fretboard_frame.pack()

    def update_fretboard(self, tuning, root, note_collection):
        pass


class FretboardFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
