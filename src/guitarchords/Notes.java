package guitarchords;

public class Notes {

	/*
	 * Notes are integers relative to C4, The note on the third fret of the A
	 * string on a standard-tuned guitar, noting that guitar music is often
	 * written an octave higher.
	 */

	// static String[] names = { "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb",
	// "G", "G#/Ab", "A", "A#/Bb", "B" };
	static String[] names = { "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B" };
	static String[] alternateNames = { null, "Db", null, "Eb", null, null, "Gb", null, "Ab", null, "Bb", null };

	static String[] degrees = { "R", "2-", "2+", "3-", "3+", "4P", "4A/5D", "5P", "6-", "6+", "7-", "7+" };

	// degrees = ("R", "2-", "2+", "3-", "3+", "4P", "4A/5D", "5P", "6-", "6+",
	// "7-", "7+")

	public static String getNoteName(int note) {
		return names[note % 12];
	}

	public static int getNoteOctave(int note) {
		return (note / 12) + 4;
	}

	public static String getFullNoteName(int note) {
		return getNoteName(note) + String.valueOf(getNoteOctave(note));
	}
	
	public static String getDegreeName(int root, int other){
		return getDegreeName(other - root);
	}
	
	public static String getDegreeName(int interval){
		// TODO
		return "";
	}

	// public Notes() {
	// // TODO Auto-generated constructor stub
	// }

	// public static void main(String args[]) {
	// for (int i = 0; i < 25; i++) {
	// System.out.println(i + "\t" + getNoteOctave(i));
	// }
	// }
}
