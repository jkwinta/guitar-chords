import tkinter as tk

from guitar_chords.gui.fret_images import FretImages


class Fret(tk.Label):
    def __init__(self, master, decoration=None, orientation='V'):
        super().__init__(master)
        if decoration in ['bar', 'left', 'right', 'reg', ]:
            self.decoration = decoration
        else:
            self.decoration = 'reg'
        self.orientation = orientation
        self.config(borderwidth=0)
        self.set_unfretted()
        # self.config(image=get_photo_image(self.decoration, 0), borderwidth=0)

    def set_fretted(self, colour='blue'):
        self.config(image=FretImages.get_fret_photo_image(self.decoration,
                                                          colour,
                                                          self.orientation))

    def set_unfretted(self):
        self.set_fretted(colour='')
