package fretboard;

import fretboard.FretButton.FretButtonType;

public class FretboardLayout {

	/**
	 * Possible included fretboard dot decoration configurations.
	 */
	enum FretboardStyle {
		STANDARD, BLANK
	};

	/** This FretboardLayout object's style given when constructed. */
	private FretboardStyle style;

	/** This FretboardLayout object's array of FretButtonTypes */
	private FretButtonType[][] layout;

	// static HashMap<Integer, Set<Integer>> a;

	/**
	 * The constructor for a new FretboardLayout given the number of strings,
	 * number of frets, and a style for the dots.
	 * 
	 * @param numberOfStrings
	 *            The number of instrument strings to be represented.
	 * @param numberOfFrets
	 *            The number of instrument frets to be represented, the array
	 *            has 1 more row than this to accommodate representation of the
	 *            string played open.
	 * @param style
	 *            The style for this Fretboard to be built as.
	 */
	public FretboardLayout(int numberOfStrings, int numberOfFrets, FretboardStyle style) {
		this.style = style;
		// We initially set a blank layout, regardless
		this.layout = new FretButtonType[numberOfFrets + 1][numberOfStrings];
		// Bar row first:
		for (int i = 0; i < numberOfStrings; i++) {
			this.layout[0][i] = FretButtonType.BAR;
		}
		// Then the rest of the frets:
		for (int j = 1; j <= numberOfFrets; j++) {
			for (int i = 0; i < numberOfStrings; i++) {
				this.layout[j][i] = FretButtonType.REGULAR;
			}
		}
		// Now decorate according to style argument:
		if (style == FretboardStyle.STANDARD) {
			this.setStandardLayout(numberOfStrings, numberOfFrets);
		}
	}

	/**
	 * Add dot decorations to this FretboardLayout in the standard
	 * configuration.
	 * 
	 * @param numberOfStrings
	 *            The number of strings that this FretboardLayout prescribes.
	 * @param numberOfFrets
	 *            The number of frets that this FretboardLayout prescribes.
	 */
	private void setStandardLayout(int numberOfStrings, int numberOfFrets) {
		// This isn't perfect, but works for 4 and 6 strings well enough, and
		// makes some sense if you think about it.
		for (int i = 1; i <= numberOfFrets; i++) {
			int numberOfDots = standardNumberOfDots(i);
			if (numberOfDots == 1) {
				this.layout[i][numberOfStrings / 2] = FretButtonType.RIGHT_DOT;
				this.layout[i][numberOfStrings / 2 - 1] = FretButtonType.LEFT_DOT;
			} else if (numberOfDots == 2) {
				this.layout[i][numberOfStrings / 3] = FretButtonType.RIGHT_DOT;
				this.layout[i][numberOfStrings / 3 - 1] = FretButtonType.LEFT_DOT;
				this.layout[i][numberOfStrings - numberOfStrings / 3] = FretButtonType.RIGHT_DOT;
				this.layout[i][numberOfStrings - numberOfStrings / 3 - 1] = FretButtonType.LEFT_DOT;
			}
		}
	}

	/**
	 * Return the FretButtonType that this FreboardLayout has at fret fretNumber
	 * on string stringNumber.
	 * 
	 * @param stringNumber
	 *            The number of the instrument string.
	 * @param fretNumber
	 *            The number of the fret.
	 * @return The FretButtonType that occurs at fretNumber on stringNumber.
	 */
	public FretButtonType getTypeAt(int stringNumber, int fretNumber) {
		return this.layout[fretNumber][stringNumber];
	}

	/**
	 * Return this FretboardLayout object's FretboardStyle.
	 * 
	 * @return The FretboardStyle of this FretboardLayout.
	 */
	public FretboardStyle getStyle() {
		return this.style;
	}

	/**
	 * Return the number of strings that this FretboardLayout prescribes.
	 * 
	 * @return The number instrument strings represented in this
	 *         FretboardLayout.
	 */
	public int getNumberOfStrings() {
		return this.layout[0].length;
	}

	/**
	 * Return the number of frets that this FretboardLayout prescribes.
	 * 
	 * @return The number of frets represented in this FretboardLayout.
	 */
	public int getNumberOfFrets() {
		return this.layout.length - 1;
	}

	/**
	 * Return the number of dots that appear on fret fretNumber of a standard
	 * guitar or bass.
	 * 
	 * @param fretNumber
	 *            The number of the fret.
	 * @return The number of dots that appear on a standard fretboard layout at
	 *         fret fretNumber.
	 */
	private static int standardNumberOfDots(int fretNumber) {
		int mod12 = fretNumber % 12;
		if (mod12 == 0) {
			return 2;
		} else if (mod12 % 2 == 1 && mod12 % 10 != 1) {
			// modulo 12 preserves parity. We want a single dot where odd and
			// not 1 or 11
			return 1;
		}
		return 0;
	}

	// Set<Integer> singleDot = new HashSet<Integer>(Arrays.asList(3, 5, 7, 9,
	// 15, 17, 19, 21));
	// Set<Integer> doubleDot = new HashSet<Integer>(Arrays.asList(12, 24));

	public static void main(String args[]){
		System.out.println("Test");
		FretboardLayout A = new FretboardLayout(6, 21, FretboardStyle.STANDARD);
		for (int i = 0; i <= A.getNumberOfFrets(); i++){
			for (int j = 0; j < A.getNumberOfStrings(); j++){
				System.out.print(A.getTypeAt(j, i) + " ");
			}
			System.out.println("");
		}
	}
}
