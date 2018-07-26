# About:
# Notes are integers relative to C4, The note on the third fret of the A string
# on a standard-tuned guitar, noting that guitar music is often written an
# octave higher.

NOTES = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', ]


class Key:
    def __init__(self, key=None):
        self.key = key

    def octave(self, note):
        return (note // 12) + 4

    def note_name(self, note):
        return NOTES[note // 12]

    def full_note_name(self, note):
        return self.note_name(note) + str(self.octave(note))
