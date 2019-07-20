# About:
# Notes are integers relative to C3, The note on the third fret of the A string
# on a standard-tuned guitar, noting that guitar music is often written an
# octave higher.


NOTES = [['C'],
         ['C#', 'Db'],
         ['D'],
         ['D#', 'Eb'],
         ['E'],
         ['F'],
         ['F#', 'Gb'],
         ['G'],
         ['G#', 'Ab'],
         ['A'],
         ['A#', 'Bb'],
         ['B'],
         ]

NATURALS = [note_list[0] if len(note_list) == 1 else None
            for note_list in NOTES]


def octave(note_index):
    return (note_index // 12) + 3


def note_names(note_index):
    return NOTES[note_index % 12]


def note_index_to_name(note_index):
    return note_names(note_index)[0] + str(octave(note_index))


def note_name_to_index(note_name):
    note_name = note_name.strip()
    note_natural = note_name[0]
    if note_natural not in 'ABCDEFG':
        raise ValueError('Note name needs to start with a character A-G.')
    if len(note_name) == 1:
        return NATURALS.index(note_natural)
    if note_name[1] == '#' or note_name[1] == 'b':
        accidental_end = 2
        while (accidental_end < len(note_name)
               and note_name[1] == note_name[accidental_end]):
            accidental_end += 1
        accidental_str = note_name[1:accidental_end]
        if note_name[1] == '#':
            accidental_increment = len(accidental_str)
        else:
            accidental_increment = -len(accidental_str)
    else:
        accidental_increment = 0
    octave_start = 0
    while set(note_name[octave_start - 1:]) <= set('-1234567890'):
        octave_start -= 1
    if octave_start:
        octave_value = int(note_name[octave_start:])
    else:
        octave_value = None
    relative_value = NATURALS.index(note_natural) + accidental_increment
    # Note: if no octave is provided, the return value is in [0:12)
    if octave_value is None:
        return relative_value % 12
    else:
        return relative_value + 12 * (octave_value - 3)


names_to_semitones = {
    'ROOT': 0,
    'MINOR 2ND': 1,
    'MAJOR 2ND': 2,
    'AUGMENTED 2ND': 3,
    'MINOR 3RD': 3,
    'MAJOR 3RD': 4,
    'PERFECT 4TH': 5,
    'AUGMENTED 4TH': 6,
    'DIMINISHED 5TH': 6,
    'PERFECT 5TH': 7,
    'AUGMENTED 5TH': 8,
    'MINOR 6TH': 8,
    'MAJOR 6TH': 9,
    'DIMINISHED 7TH': 9,
    'MINOR 7TH': 10,
    'MAJOR 7TH': 11,
    'MAJOR 9TH': 14,
    'PERFECT 11TH': 17,
    'SHARP 11TH': 18,
    'MAJOR 13th': 21,
}

if __name__ == '__main__':
    for i in range(-10, 100):
        if i != note_name_to_index(note_index_to_name(i)):
            print(i, note_index_to_name(i))
    pass
