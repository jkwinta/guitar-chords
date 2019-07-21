import tkinter as tk
from PIL import Image, ImageTk
from os import path

IMAGE_DIR = './files/fret_icons/png'

IMAGE_PATHS_BY_DECORATOR = {
    'bar': ['bar', 'bar_fretted'],
    'left': ['left', 'left_fretted'],
    'right': ['right', 'right_fretted'],
    'reg': ['reg', 'reg_fretted'],
}

PHOTO_IMAGES_BY_DECORATOR = {
    deco: [None for _ in ims] for deco, ims in IMAGE_PATHS_BY_DECORATOR.items()
}


def get_photo_image(decoration, status):
    if PHOTO_IMAGES_BY_DECORATOR[decoration][bool(status)] is None:
        image_name = IMAGE_PATHS_BY_DECORATOR[decoration][bool(status)]
        image_path = path.join(IMAGE_DIR, image_name + '.png')
        result = ImageTk.PhotoImage(Image.open(image_path))
        PHOTO_IMAGES_BY_DECORATOR[decoration][bool(status)] = result
    return PHOTO_IMAGES_BY_DECORATOR[decoration][bool(status)]


# ImageTk.PhotoImage(Image.open(path.join(IMAGE_DIR, im + '.png')))


class Fret(tk.Label):
    def __init__(self, master, decoration):
        super().__init__(master)
        if decoration in IMAGE_PATHS_BY_DECORATOR:
            self.decoration = decoration
        else:
            self.decoration = 'reg'
        self.config(image=get_photo_image(self.decoration, 0), borderwidth=0)

    def set_fretted(self):
        self.config(image=get_photo_image(self.decoration, 1))

    def set_unfretted(self):
        self.config(image=get_photo_image(self.decoration, 0))
