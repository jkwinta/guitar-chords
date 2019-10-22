from guitar_chords.chords import chords
from guitar_chords.scales import scales
from guitar_chords.notes import note_name_to_index, degree_note_name
from guitar_chords.relative_note_collection import RelativeNoteCollection


class KeyedNoteCollection:

    def __init__(self, root_name, scale_or_chord, collection_name):
        self.root_name = root_name
        self.root_value = note_name_to_index(self.root_name)
        self.scale_or_chord = scale_or_chord
        self.collection_name = collection_name
        self.relative_note_collection = RelativeNoteCollection(scale_or_chord,
                                                               collection_name)
        self.chords_contained = None
        self.scales_containing = None

    def __str__(self):
        return ' '.join(w.capitalize() for w in (
                [self.root_name]
                + self.collection_name.split(' ')
                + [self.scale_or_chord])
                        )

    def __repr__(self):
        return self.__class__.__name__ + str(
            (self.root_name, self.scale_or_chord, self.collection_name))

    def get_note_values(self):
        return [(note_val + self.root_value) % 12
                for note_val in self.relative_note_collection.get_note_values()]

    def get_chords_contained(self):
        if self.chords_contained is None:
            self.chords_contained = []
            for degree_name in self.relative_note_collection.get_note_names():
                degree_root_note = degree_note_name(self.root_name, degree_name)
                for chord_name in chords:
                    chord = KeyedNoteCollection(degree_root_note, 'chord',
                                                chord_name)
                    if set(chord.get_note_values()) <= set(
                            self.get_note_values()):
                        self.chords_contained.append(chord)
        return self.chords_contained

    def get_scales_containing(self):
        if self.scales_containing is None:
            pass
        return self.scales_containing


if __name__ == '__main__':
    a = KeyedNoteCollection('C', 'chord', 'MAJOR')
    print(a)
