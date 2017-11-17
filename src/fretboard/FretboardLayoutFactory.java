package fretboard;

import java.util.HashMap;

import fretboard.FretButton.FretButtonType;

public class FretboardLayoutFactory {

	public FretboardLayoutFactory() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * Possible included fretboard dot decoration configurations.
	 */
	static enum FretboardStyle {
		STANDARD
	};

	static HashMap<Integer, Integer> a;

	static FretButtonType[][] getLayout(int numberOfStrings, int numberOfFrets, FretboardStyle style) {
		if (style == FretboardStyle.STANDARD) {
			return getStandardLayout(numberOfStrings, numberOfFrets);
		}
		FretButtonType[][] layout = new FretButtonType[numberOfFrets][numberOfStrings];
		return layout;
	}

	private static FretButtonType[][] getStandardLayout(int numberOfStrings, int numberOfFrets) {
		FretButtonType[][] layout = new FretButtonType[numberOfFrets][numberOfStrings];
		layout[0] = getBarRow(numberOfStrings);
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

}
