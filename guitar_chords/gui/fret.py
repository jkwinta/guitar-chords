import tkinter as tk
from PIL import Image, ImageTk
from os import path

IMAGE_DIR = '../files/fret_icons/png'

IMAGE_PATHS_BY_DECORATOR = {
    'bar': ['bar', 'bar_fretted'],
    # 'left': ['left', 'left_fretted'],
    # 'right': ['right', 'right_fretted'],
    # 'reg': ['reg', 'reg_fretted'],
    'left': ['left', 'left_fretted_smbc'],
    'right': ['right', 'right_fretted_smbc'],
    'reg': ['reg', 'reg_fretted_smbc'],
}

IMAGE_PATHS = {
    ('bar', True): 'bar_fretted',
    ('bar', False): 'bar',
    ('left', True): 'left_fretted_smbc',
    ('left', False): 'left',
    ('right', True): 'right_fretted_smbc',
    ('right', False): 'right',
    ('reg', True): 'reg_fretted_smbc',
    ('reg', False): 'reg',
}

PHOTO_IMAGES_BY_DECORATOR = {
    deco: [None for _ in ims] for deco, ims in IMAGE_PATHS_BY_DECORATOR.items()
}

PHOTO_IMAGES = {}


# TODO: THis function converts V/H to 0/90???
def get_photo_image(decoration, is_fretted, rotation):
    key = decoration, is_fretted, rotation
    if key not in PHOTO_IMAGES:
        image_name = IMAGE_PATHS[key[:2]]
        image_path = path.join(IMAGE_DIR, image_name + '.png')
        image = Image.open(image_path).rotate(rotation, expand=True)
        photo_image = ImageTk.PhotoImage(image)
        PHOTO_IMAGES[key] = photo_image
    return PHOTO_IMAGES[key]


# ImageTk.PhotoImage(Image.open(path.join(IMAGE_DIR, im + '.png')))


class Fret(tk.Label):
    def __init__(self, master, decoration, orientation='V'):
        super().__init__(master)
        if decoration in IMAGE_PATHS_BY_DECORATOR:
            self.decoration = decoration
        else:
            self.decoration = 'reg'
        self.orientation = orientation
        if orientation == 'V':
            self.rotation = 0
        elif orientation == 'H':
            self.rotation = 90
        self.config(borderwidth=0)
        self.set_unfretted()
        # self.config(image=get_photo_image(self.decoration, 0), borderwidth=0)

    def set_fretted(self):
        self.config(image=get_photo_image(self.decoration, 1, self.rotation))

    def set_unfretted(self):
        self.config(image=get_photo_image(self.decoration, 0, self.rotation))
