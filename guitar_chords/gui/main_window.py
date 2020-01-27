import tkinter as tk

from guitar_chords.gui.browse_note_collections import \
    BrowseNoteCollectionToplevel, BrowseNoteCollection


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.asdflkjsdf = master
        self.chords_button = tk.Button(self, text='Collect chords',
                                       command=self.chords_callback)
        self.chords_button.pack()
        self.scale_button = tk.Button(self, text='Start with scale',
                                      command=self.scale_callback)
        self.scale_button.pack()
        self.or_label = tk.Label(self, text='or...')
        self.or_label.pack()
        self.browse_button = tk.Button(self, text='Browse chords and scales',
                                       command=self.browse_callback)
        self.browse_button.pack()
        self.pack()

    def chords_callback(self):
        pass

    def scale_callback(self):
        pass

    def browse_callback(self):
        ModalWindow(self, BrowseNoteCollection)


class ModalWindow(tk.Toplevel):
    def __init__(self, master, frame_type=None):
        super().__init__(master)
        if frame_type is None:
            self.content = None
        else:
            self.content = frame_type(self)
            self.content.pack()

            self.grab_set()
            self.protocol("WM_DELETE_WINDOW", self.cancel)
            self.focus_set()
            self.wait_window(self)

    def cancel(self):
        self.master.focus_set()
        self.destroy()
