from guitar_chords.note_collection import Chord, Scale
from guitar_chords.scales import scales


class ChordCollection:

    def __init__(self):
        self.chords = []
        self.all_notes = None
        self.scales_contained_by = None
        self.nearest_scales = None

    def add_chord(self, root_name, chord_name):
        self.chords.append(Chord(root_name, chord_name))
        self.all_notes = None
        self.scales_contained_by = None
        self.nearest_scales = None

    def get_all_notes(self):
        if self.all_notes is None:
            self.all_notes = []
            for chord in self.chords:
                self.all_notes.extend(note.value for note in chord.notes)
        return self.all_notes

    def get_scales_contained_by(self):
        if self.scales_contained_by is None:
            self.scales_contained_by = []
            all_notes_set = set(self.get_all_notes())
            for chord in self.chords:
                root_note = chord.root_note
                for scale_name in scales.keys():
                    scale = Scale(root_note.name, scale_name)
                    if all_notes_set <= set(scale.get_note_values()):
                        self.scales_contained_by.append(scale)
        return self.scales_contained_by

    def get_nearest_scales(self):
        if self.nearest_scales is None:
            scored_scales = []
            for chord in self.chords:
                root_note = chord.root_note
                for scale_name in scales.keys():
                    scale = Scale(root_note.name, scale_name)
                    score_hits = 0
                    for note in self.get_all_notes():
                        if note in scale.get_note_values():
                            score_hits += 1
                    score = score_hits / len(scale.get_note_values())
                    scored_scales.append([scale, score])
            self.nearest_scales = sorted(scored_scales, key=lambda x: x[-1],
                                         reverse=True)
        return self.nearest_scales


if __name__ == '__main__':
    cc = ChordCollection()
    cc.add_chord('F', 'MINOR 7TH')
    cc.add_chord('Bb', 'MAJOR')
    print('a')
