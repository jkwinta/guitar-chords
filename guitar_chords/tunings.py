from guitar_chords.notes import note_name_to_index

tunings = {
    'STANDARD': ('E2', 'A2', 'D3', 'G3', 'B3', 'E4'),
    'OPEN E': ('E2', 'B2', 'E3', 'G#3', 'B3', 'E4'),
    'OPEN D': ('D2', 'A2', 'D3', 'F#3', 'A3', 'D4'),
    'OPEN A': ('E2', 'A2', 'E3', 'A3', 'C#4', 'E4'),
    'OPEN G': ('D2', 'G2', 'D3', 'G3', 'B3', 'D4'),
    'OPEN G LOW E': ('E2', 'G2', 'D3', 'G3', 'B3', 'D4'),
    'G6': ('D2', 'G2', 'D3', 'G3', 'B3', 'E4'),
    'DADGAD': ('D2', 'A2', 'D3', 'G3', 'A3', 'D4'),
    'DROP D': ('D2', 'A2', 'D3', 'G3', 'B3', 'E4'),
    'DOUBLE DROP D': ('D2', 'A2', 'D3', 'G3', 'B3', 'D4'),

}


class Tuning:

    def __init__(self, tuning_name='STANDARD'):
        self.tuning_name = tuning_name
        self.tuning = tunings[tuning_name]
        self.tuning_values = tuple(note_name_to_index(n) for n in self.tuning)

    def __repr__(self):
        return 'Tuning({})'.format(self.tuning_name)

    def __str__(self):
        return '{} tuning'.format(' '.join(
            word.capitalize() for word in self.tuning_name.split())
        )

    def get_fret_note(self, string_number, fret_number):
        return self.tuning_values[string_number] + fret_number


# TODO: Check:
tuning_frettings = {
    'STANDARD': (0, 0, 0, 0, 0, 0),
    'OPEN E': (0, 2, 2, 1, 0, 0),
    'OPEN D': (-2, 0, 0, -1, -2, -2),
    'OPEN A': (0, 0, 2, 2, 2, 0),
    'OPEN G': (-2, -2, 0, 0, 0, -2),
    'OPEN G LOW E': (0, -2, 0, 0, 0, -2),
    'G6': (-2, -2, 0, 0, 0, 0),
    'DADGAD': (-2, 0, 0, 0, -2, -2),
    'DROP D': (-2, 0, 0, 0, 0, 0),
    'DOUBLE DROP D': (-2, 0, 0, 0, 0, -2),
}
