import tkinter as tk

from .. import NOTES

N_COLUMNS = 3


class SelectRootNoteFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root_notes_label = tk.Label(self, text="Root note")
        self.root_note_button_frame = tk.Frame(self)
        self.root_note_var = tk.StringVar()
        self.root_note_var.set(None)
        # Add buttons
        i = 0
        for note_equivalences in NOTES:
            for note in note_equivalences:
                b = tk.Radiobutton(self.root_note_button_frame, text=note,
                                   variable=self.root_note_var, value=note)
                b.grid(row=i // N_COLUMNS, column=i % N_COLUMNS,
                       sticky=tk.W, padx=5, pady=2)
                i += 1
        self.root_notes_label.pack()
        self.root_note_button_frame.pack()

    def get_selected_note(self):
        return self.root_note_var.get()
        # selection_tuple = self.root_notes_list_box.curselection()
        # if selection_tuple:
        #     result = self.note_names[selection_tuple[0]]
        # else:
        #     result = None
        # return result
