import tkinter as tk

from guitar_chords.gui.select_root_note_frame import SelectRootNoteFrame
from guitar_chords.gui.select_note_collection_frame import \
    SelectNoteCollectionFrame
from guitar_chords.gui.fretboard import FretboardToplevel
from guitar_chords.gui.select_tuning_frame import SelectTuningFrame
from guitar_chords.gui.fretboard_orientation_select_frame import \
    FretboardOrientationSelectFrame
from guitar_chords.note_collection import Chord, Scale


class BrowseNoteCollection(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Add root note select:
        self.root_select = SelectRootNoteFrame(self)
        self.root_select.pack()
        self.note_collection_select = SelectNoteCollectionFrame(self)
        self.note_collection_select.pack(fill=tk.X)
        self.tuning_select = SelectTuningFrame(self)
        self.tuning_select.pack(fill=tk.X)
        self.orientation_select = FretboardOrientationSelectFrame(self)
        self.orientation_select.pack(fill=tk.X)
        self.go_button = tk.Button(self, text='Go!',
                                   command=self.go_button_callback)
        self.go_button.pack()
        # self.config(background='gray80')
        self.fretboard = None

    def go_button_callback(self):
        # print(self.root_select.get_selected_note(),
        #       self.note_collection_select.get_selected_note_collection_name(),
        #       self.note_collection_select.get_selected_note_collection(),
        #       flush=True)
        tuning = self.tuning_select.get_selected_tuning()
        root_note = self.root_select.get_selected_note()
        chord_or_scale = self.note_collection_select.get_chord_or_scale()
        if chord_or_scale == 'chord':
            chord_name = self.note_collection_select.get_selected_note_collection_name()
            note_collection = Chord(root_note, chord_name)
        elif chord_or_scale == 'scale':
            scale_name = self.note_collection_select.get_selected_note_collection_name()
            note_collection = Scale(root_note, scale_name)
        else:
            note_collection = None
        # print(note_collection)
        # print(note_collection.intervals if note_collection is not None else None)
        orientation = self.orientation_select.get_orientation()
        # print(tuning, type(tuning))
        if tuning is None or note_collection is None:
            pass
        else:
            if self.fretboard is None or not self.fretboard.winfo_exists():
                self.fretboard = FretboardToplevel(self, orientation)
                self.fretboard.update_fretboard(tuning, note_collection)
            else:
                if orientation == self.fretboard.get_orientation():
                    self.fretboard.update_fretboard(tuning, note_collection)
                else:
                    self.fretboard.destroy()
                    self.fretboard = FretboardToplevel(self, orientation)
                    self.fretboard.update_fretboard(tuning, note_collection)


class BrowseNoteCollectionToplevel(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.browse_note_collection_frame = BrowseNoteCollection(self)
        self.browse_note_collection_frame.pack()
