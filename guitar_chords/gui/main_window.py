import tkinter as tk

from guitar_chords.notes import NOTES
from .select_root_note_frame import SelectRootNoteFrame
from .select_note_collection_frame import SelectNoteCollectionFrame
from .fretboard import Fretboard


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Add root note select:
        self.root_select = SelectRootNoteFrame(self)
        self.root_select.pack()
        self.note_collection_select = SelectNoteCollectionFrame(self)
        self.note_collection_select.pack(fill=tk.X)
        self.go_button = tk.Button(self, text='Go!',
                                   command=self.go_button_callback)
        self.go_button.pack()
        self.pack()
        self.fretboard = None

    def go_button_callback(self):
        print(self.root_select.get_selected_note(),
              self.note_collection_select.get_selected_note_collection_name(),
              self.note_collection_select.get_selected_note_collection(),
              flush=True)
        tuning = 'STANDARD'  # TODO
        root = self.root_select.get_selected_note()
        note_collection = (
            self.note_collection_select.get_chord_or_scale(),
            self.note_collection_select.get_selected_note_collection_name()
        )
        if tuning is None or root is None or None in note_collection:
            pass
        else:
            if self.fretboard is None or not self.fretboard.winfo_exists():
                self.fretboard = Fretboard(self, tuning, root, note_collection, 'H')
            else:
                self.fretboard.update_fretboard(tuning, root, note_collection)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.wm_title('MaiWindow title str')
    root.mainloop()
