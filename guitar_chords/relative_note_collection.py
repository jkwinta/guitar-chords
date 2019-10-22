from guitar_chords.scales import scales
from guitar_chords.chords import chords
from guitar_chords.notes import names_to_semitones


class RelativeNoteCollection:
    """Represents a scale or chord"""

    def __init__(self, scale_or_chord, collection_name):
        self.scale_or_chord = scale_or_chord
        self.collection_name = collection_name
        if scale_or_chord == 'scale':
            self.note_collection = scales[collection_name]
        elif scale_or_chord == 'chord':
            self.note_collection = chords[collection_name]
        else:
            self.note_collection = []

    def __str__(self):
        return ' '.join(w.captialize() for w in (
                self.collection_name.split(' ') + [self.scale_or_chord]))

    def __repr__(self):
        return self.__class__.__name__ + str(
            (self.scale_or_chord, self.collection_name))

    def get_note_names(self):
        return self.note_collection

    def get_note_values(self):
        return [names_to_semitones[nn] for nn in self.get_note_names()]
