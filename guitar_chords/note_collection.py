from guitar_chords.chords import chords
from guitar_chords.scales import scales
from guitar_chords.notes import IntervalNote


class KeyedNoteCollection:

    def __init__(self, root_name, list_of_interval_names):
        self.root_name = root_name
        self.root_note = None
        self.intervals = list_of_interval_names
        self.notes = []
        for interval_name in list_of_interval_names:
            self.notes.append(IntervalNote(root_name, interval_name))
            if interval_name == 'ROOT':
                self.root_note = self.notes[-1]
        if self.root_note is None:
            self.root_note = IntervalNote(root_name, 'ROOT')

        self.chords_contained = None
        self.chords_contained_by = None
        self.scales_contained = None
        self.scales_contained_by = None

    def get_note_values(self):
        return [note.value for note in self.notes]

    def contains_collection(self, other):
        return set(other.get_note_values()) <= set(self.get_note_values())

    def is_contained_by_collection(self, other):
        return set(self.get_note_values()) <= set(other.get_note_values())

    def get_chords_contained(self):
        if self.chords_contained is None:
            self.chords_contained = []
            for note in self.notes:
                for chord_name in chords.keys():
                    chord = Chord(note.name, chord_name)
                    if self.contains_collection(chord):
                        self.chords_contained.append(chord)
        return self.chords_contained

    def get_chords_contained_by(self):
        if self.chords_contained_by is None:
            self.chords_contained_by = []
            for note in self.notes:
                for chord_name in chords.keys():
                    chord = Chord(note.name, chord_name)
                    if self.is_contained_by_collection(chord):
                        self.chords_contained_by.append(chord)
        return self.chords_contained_by

    def get_scales_contained(self):
        if self.scales_contained is None:
            self.scales_contained = []
            for note in self.notes:
                for scale_name in scales.keys():
                    scale = Scale(note.name, scale_name)
                    if self.contains_collection(scale):
                        self.scales_contained.append(scale)
        return self.scales_contained

    def get_scales_contained_by(self):
        if self.scales_contained_by is None:
            self.scales_contained_by = []
            for note in self.notes:
                for scale_name in scales.keys():
                    scale = Scale(note.name, scale_name)
                    if self.is_contained_by_collection(scale):
                        self.scales_contained_by.append(scale)
        return self.scales_contained_by


class Chord(KeyedNoteCollection):
    def __init__(self, root_name, chord_name):
        super().__init__(root_name, chords.get(chord_name, []).copy())
        self.chord_name = chord_name

    def __str__(self):
        return ' '.join(
            word.capitalize() for word in
            [self.root_name] + self.chord_name.split(' ') + ['Chord'])

    def __repr__(self):
        return 'Chord({}, {})'.format(self.root_name, self.chord_name)


class Scale(KeyedNoteCollection):
    def __init__(self, root_name, scale_name):
        super().__init__(root_name, scales.get(scale_name, []).copy())
        self.scale_name = scale_name

    def __str__(self):
        return ' '.join(
            word.capitalize() for word in
            [self.root_name] + self.scale_name.split(' ') + ['Scale'])

    def __repr__(self):
        return 'Scale({}, {})'.format(self.root_name, self.scale_name)


if __name__ == '__main__':
    a = Chord('C', 'MAJOR')
    b = Scale('D', 'MINOR PENTATONIC')
    print(a)
