import tkinter as tk

from guitar_chords.notes import NOTES
from .select_root_note_frame import SelectRootNoteFrame


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Add root note select:
        self.root_select = SelectRootNoteFrame(self)
        self.root_select.pack()
        self.go_button = tk.Button(self, text='Go!',
                                   command=self.go_button_callback)
        self.go_button.pack()
        self.pack()

    def go_button_callback(self):
        note_selection = self.root_select.get_selected_note()
        print('You have selected "{}"'.format(note_selection), flush=True)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    root.wm_title('MaiWindow title str')
    root.mainloop()
