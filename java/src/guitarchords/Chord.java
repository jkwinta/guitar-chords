package guitarchords;

public class Chord {

	private int[] tuning;
	private int[] fretted;
	private Integer[] notes;
	private int numberOfStrings;

	public Chord(int numberOfStrings) {
		this.numberOfStrings = numberOfStrings;
		this.tuning = new int[numberOfStrings];
		this.fretted = new int[numberOfStrings];
		this.notes = new Integer[numberOfStrings];
	}

	private void updateNotes() {
		for (int i = 0; i < numberOfStrings; i++) {
			updateNote(i);
		}
	}

	private void updateNote(int i) {
		if (fretted[i] < 0) {
			notes[i] = null;
		} else {
			notes[i] = tuning[i] + fretted[i];
		}
	}

}
