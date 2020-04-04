import pathlib
import PIL.Image
import PIL.ImageTk


class FretImages:
    image_base_path = None
    image_paths = {}
    images = {}

    @staticmethod
    def get_image_base_path():
        if FretImages.image_base_path is None:
            path = pathlib.Path(__file__).absolute()
            while path != path.parent and path.name != 'guitar_chords':
                path = path.parent
            FretImages.image_base_path = path.parent / 'files/fret_icons/gif'
        return FretImages.image_base_path

    @staticmethod
    def get_file_path(decoration, fretted_colour):
        key = (decoration, fretted_colour)
        if key not in FretImages.image_paths:
            if not fretted_colour:
                result = FretImages.get_image_base_path() / '{}.gif'.format(decoration)
            else:
                result = FretImages.get_image_base_path() / fretted_colour / '{}_fretted.gif'.format(decoration)
            FretImages.image_paths[key] = result
        return FretImages.image_paths[key]

    @staticmethod
    def get_fret_photo_image(decoration, fretted_colour, orientation):
        key = (decoration, fretted_colour, orientation)
        if key not in FretImages.images:
            file_path = FretImages.get_file_path(decoration, fretted_colour)
            if orientation == 'V':
                rotation = 0
            elif orientation == 'H':
                rotation = 90
            else:
                return None
            image = PIL.Image.open(file_path).rotate(rotation, expand=True)
            photo_image = PIL.ImageTk.PhotoImage(image)
            FretImages.images[key] = photo_image
        return FretImages.images[key]


if __name__ == '__main__':
    print(FretImages.get_image_base_path())
