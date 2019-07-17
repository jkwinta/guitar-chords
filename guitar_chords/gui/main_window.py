import tkinter as tk

from guitar_chords.notes import NOTES
from .select_root_note_frame import SelectRootNoteFrame
from .note_collection_select_frame import NoteCollectionSelectFrame


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Add root note select:
        self.root_select = SelectRootNoteFrame(self)
        self.root_select.pack()
        self.note_collection_select = NoteCollectionSelectFrame(self)
        self.note_collection_select.pack(fill=tk.X)
        self.go_button = tk.Button(self, text='Go!',
                                   command=self.go_button_callback)
        self.go_button.pack()
        self.pack()

    def go_button_callback(self):
        print(self.root_select.get_selected_note(),
              self.note_collection_select.get_selected_note_collection_name(),
              self.note_collection_select.get_selected_note_collection(),
              flush=True)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.wm_title('MaiWindow title str')
    root.mainloop()
