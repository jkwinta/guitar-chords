package fretboard;

import fretboard.FretButton.FretButtonType;

public class FretboardLayout {

	/**
	 * Possible included fretboard dot decoration configurations.
	 */
	enum FretboardStyle {
		STANDARD, BLANK
	};

	private FretButtonType[][] layout;
	private FretboardStyle style;

	// static HashMap<Integer, Set<Integer>> a;

	public FretboardLayout(int numberOfStrings, int numberOfFrets, FretboardStyle style) {
		this.layout = new FretButtonType[numberOfFrets + 1][numberOfStrings];
		this.style = style;
	}

	/**
	 * Return a FretboardLayout
	 * 
	 * @param numberOfStrings
	 * @param numberOfFrets
	 * @param style
	 * @return
	 */
	static FretButtonType[][] getFretboardLayout(int numberOfStrings, int numberOfFrets, FretboardStyle style) {
		if (style == FretboardStyle.STANDARD) {
			return getStandardLayout(numberOfStrings, numberOfFrets);
		}
		FretButtonType[][] layout = new FretButtonType[numberOfFrets + 1][numberOfStrings];
		return layout;
	}

	private static FretButtonType[][] getStandardLayout(int numberOfStrings, int numberOfFrets) {
		FretButtonType[][] layout = new FretButtonType[numberOfFrets + 1][numberOfStrings];
		layout[0] = getBarRow(numberOfStrings);
		for (int i = 1; i < numberOfFrets + 1; i++) {
			layout[i] = getDottedRow(getNumberOfDots(i, FretboardStyle.STANDARD), numberOfStrings);
		}
		return layout;
	}

	private static FretButtonType[] getBarRow(int numberOfStrings) {
		FretButtonType[] row = new FretButtonType[numberOfStrings];
		for (int i = 0; i < numberOfStrings; i++) {
			row[i] = FretButtonType.BAR;
		}
		return row;
	}

	private static int getNumberOfDots(int fretNumber, FretboardStyle style) {
		if (style == FretboardStyle.STANDARD) {
			if (fretNumber % 12 == 0) {
				return 2;
			} else if (fretNumber % 2 == 1 && (fretNumber + 1) % 12 != 0 && (fretNumber - 1) % 12 != 0) {
				return 1;
			} else {
				return 0;
			}
		}
		return 0;
	}

	private static FretButtonType[] getDottedRow(int numberOfDots, int numberOfStrings) {
		if (numberOfDots == 1 && numberOfStrings == 6) {
			return new FretButtonType[] { FretButtonType.REGULAR, FretButtonType.REGULAR, FretButtonType.LEFT_DOT,
					FretButtonType.RIGHT_DOT, FretButtonType.REGULAR, FretButtonType.REGULAR };
		} else if (numberOfDots == 2 && numberOfStrings == 6) {
			return new FretButtonType[] { FretButtonType.REGULAR, FretButtonType.LEFT_DOT, FretButtonType.RIGHT_DOT,
					FretButtonType.LEFT_DOT, FretButtonType.RIGHT_DOT, FretButtonType.REGULAR };
		} else if (numberOfDots == 1 && numberOfStrings == 4) {
			return new FretButtonType[] { FretButtonType.REGULAR, FretButtonType.LEFT_DOT, FretButtonType.RIGHT_DOT,
					FretButtonType.REGULAR };
		} else if (numberOfDots == 2 && numberOfStrings == 4) {
			return new FretButtonType[] { FretButtonType.LEFT_DOT, FretButtonType.RIGHT_DOT, FretButtonType.LEFT_DOT,
					FretButtonType.RIGHT_DOT };
		}
		FretButtonType[] row = new FretButtonType[numberOfStrings];
		for (int i = 0; i < numberOfStrings; i++) {
			row[i] = FretButtonType.REGULAR;
		}
		return row;
	}

	// Set<Integer> singleDot = new HashSet<Integer>(Arrays.asList(3, 5, 7, 9,
	// 15, 17, 19, 21));
	// Set<Integer> doubleDot = new HashSet<Integer>(Arrays.asList(12, 24));

}
