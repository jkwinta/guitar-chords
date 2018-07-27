STANDARD = [0] * 6
STANDARD[1] = -3
STANDARD[0] = STANDARD[1] - 5
STANDARD[2] = STANDARD[1] + 5
STANDARD[3] = STANDARD[2] + 5
STANDARD[4] = STANDARD[3] + 4
STANDARD[5] = STANDARD[4] + 5
STANDARD = tuple(STANDARD)

OPEN_E = tuple(i + j for i, j in zip(STANDARD, [0, 2, 2, 1, 0, 0]))
OPEN_D = tuple(i - 2 for i in OPEN_E)

OPEN_A = tuple(i + j for i, j in zip(STANDARD, [0, 0, 2, 2, 2, 0]))
OPEN_G = tuple(i - 2 for i in OPEN_A)

G6 = tuple(i + j for i, j in zip(STANDARD, [-2, -2, 0, 0, 0, 0]))

# C6: C-A-C-G-C-E
# G6: D-G-D-G-B-E
# DADGAD

from python_guitar_chords import notes

for i in G6:
    print(notes.Key().full_note_name(i))
