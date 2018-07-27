# About:
# Notes are integers relative to C4, The note on the third fret of the A string
# on a standard-tuned guitar, noting that guitar music is often written an
# octave higher.

NOTES = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', ]

NOTE_INDEX = {}
for i in range(len(NOTES)):
    NOTE_INDEX[NOTES[i]] = i
    

class Key:
    def __init__(self, key=None):
        self.key = key

    def octave(self, note):
        return (note // 12) + 4

    def note_name(self, note):
        return NOTES[note % 12]

    def full_note_name(self, note):
        return self.note_name(note) + str(self.octave(note))

    def note_from_name(self, note_name):
        if set(note_name) < set.union(set('1234567890'), *(set(n) for n in NOTES)):
            pass
