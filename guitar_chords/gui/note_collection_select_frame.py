import tkinter as tk

from .. import chords, scales


class NoteCollectionSelectFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.chord_or_scale_frame = tk.Frame(self)
        self.chord_or_scale = tk.StringVar()
        self.chord_or_scale.set(None)
        for text, value in [('Scales', 'scale'), ('Chords', 'chord')]:
            b = tk.Radiobutton(self.chord_or_scale_frame, text=text,
                               variable=self.chord_or_scale, value=value,
                               command=self._on_button_click)
            b.config(indicatoron=0)
            b.pack(side=tk.LEFT)
        self.chord_or_scale_frame.pack()
        self.note_collection_names = None
        self.note_collections = None
        self.note_collection_list_box = tk.Listbox(self)
        self.note_collection_list_box.pack()

    def _on_button_click(self):
        if self.chord_or_scale.get() == 'scale':
            self.note_collections = scales
        elif self.chord_or_scale.get() == 'chord':
            self.note_collections = chords
        else:
            self.note_collections = None
        self.note_collection_list_box.delete(0, tk.END)
        if self.note_collections is not None:
            self.note_collection_names = []
            for collection_name in self.note_collections:
                self.note_collection_list_box.insert(
                    tk.END, ' '.join(w.capitalize()
                                     for w in collection_name.split(' '))
                )
                self.note_collection_names.append(collection_name)

    def get_selected_note_collection_name(self):
        selection_tuple = self.note_collection_list_box.curselection()
        if selection_tuple:
            result = self.note_collection_names[selection_tuple[0]]
        else:
            result = None
        return result

    def get_selected_note_collection(self):
        note_collection_name = self.get_selected_note_collection_name()
        if note_collection_name is not None:
            return self.note_collections[note_collection_name]
        return None
