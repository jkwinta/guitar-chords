package fretboard;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

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
		FretButtonType[][] layout = new FretButtonType[numberOfFrets + 1][numberOfStrings];
		return layout;
	}

	private static FretButtonType[][] getStandardLayout(int numberOfStrings, int numberOfFrets) {
		FretButtonType[][] layout = new FretButtonType[numberOfFrets + 1][numberOfStrings];
		layout[0] = getBarRow(numberOfStrings);
		for (int i = 1; i < numberOfFrets + 1; i++){
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
	
//	Set<Integer> singleDot = new HashSet<Integer>(Arrays.asList(3, 5, 7, 9, 15, 17, 19, 21));
//	Set<Integer> doubleDot = new HashSet<Integer>(Arrays.asList(12, 24));

	
	

}
