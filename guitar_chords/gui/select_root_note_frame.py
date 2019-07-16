import tkinter as tk

from .. import NOTES


class SelectRootNoteFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root_notes_label = tk.Label(self, text="Root note")
        self.root_notes_list_box = tk.Listbox(self)
        self.note_names = []
        for value, note_equivalences in enumerate(NOTES):
            for note in note_equivalences:
                self.root_notes_list_box.insert(tk.END, ' ' + note)
                self.note_names.append(note)
        self.root_notes_label.pack()
        self.root_notes_list_box.pack()

    def get_selected_note(self):
        selection_tuple = self.root_notes_list_box.curselection()
        if selection_tuple:
            result = self.note_names[selection_tuple[0]]
        else:
            result = None
        return result
