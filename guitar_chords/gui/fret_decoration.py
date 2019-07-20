BAR = 'bar'
LEFT = 'left'
RIGHT = 'right'
REG = 'reg'


class FretDecorator:

    @staticmethod
    def n_dot_row(n_dots, n_strings):
        dots = [LEFT, RIGHT] * n_dots
        regs = (n_strings - len(dots)) * [REG]
        regs_half = len(regs) // 2
        pre, post = regs[:regs_half], regs[regs_half:]
        for i, deco in enumerate(pre + dots + post):
            if i < n_strings:
                yield deco

    @staticmethod
    def standard_number_of_dots(fret_number):
        mod_12 = fret_number % 12
        if not mod_12:
            return 2
        if (mod_12 % 2) == 1 and (mod_12 % 10) != 1:
            return 1
        return 0

    def __init__(self, number_of_strings, number_of_frets):
        self.number_of_strings = number_of_strings
        self.number_of_frets = number_of_frets

    def __iter__(self):
        for string_number in range(self.number_of_strings):
            yield 0, string_number, BAR
        for fret_number in range(1, self.number_of_frets + 1):
            n_dots = self.standard_number_of_dots(fret_number)
            for string_number, deco in enumerate(self.n_dot_row(
                    n_dots, self.number_of_strings)):
                yield fret_number, string_number, deco
