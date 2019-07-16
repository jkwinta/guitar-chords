from python.gui.fret import DECORATIONS, REGULAR, LEFT_DOT, RIGHT_DOT, NUT


class FretboardDecoration:
    @staticmethod
    def get_at(string_number, fret_number):
        return None


class StandardFretboardDecoration(FretboardDecoration):

    @staticmethod
    def get_at(string_number, fret_number):
        if fret_number == 0:
            return NUT
        elif fret_number % 12 == 0:
            if string_number in (1, 3):
                return LEFT_DOT
            elif string_number in (2, 4):
                return RIGHT_DOT
        elif fret_number % 12 in (3, 5, 7, 9):
            if string_number == 2:
                return LEFT_DOT
            elif string_number == 3:
                return RIGHT_DOT
        return REGULAR
