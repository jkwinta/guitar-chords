package fretboard;

import java.awt.GridLayout;
import java.awt.HeadlessException;

import javax.swing.JFrame;

import fretboard.FretboardLayout.FretboardStyle;

/**
 * The JFrame that handles building the interactive Fretboard.
 * 
 * @author jkwinta
 *
 */
@SuppressWarnings("serial") // Not serializing, quite yet
public class InteractiveFretboard extends JFrame {

	/**
	 * The gap between components in the GridLayout. Used for both horizontal
	 * and vertical gap values. This should probably stay 0, as is.
	 */
	final static int GRID_LAYOUT_GAP = 0;

	/** The number of strings to use in the argument-less constructor. */
	final static int DEFAULT_NUMBER_OF_STRINGS = 6;

	/** The number of frets to use in the argument-less constructor. */
	final static int DEFAULT_NUMBER_OF_FRETS = 21;

	/** Array of FretObservers each representing instrument strings. */
	private FretHandler[] strings;

	/** The FretboardLayout prescribing the Icons to use for button styles. */
	private FretboardLayout layout;

	/**
	 * Constructor with no arguments uses defaults for number of strings and
	 * number of frets.
	 * 
	 * @throws HeadlessException
	 */
	InteractiveFretboard() throws HeadlessException {
		this(DEFAULT_NUMBER_OF_STRINGS, DEFAULT_NUMBER_OF_FRETS);
	}

	InteractiveFretboard(int numberOfStrings, int numberOfFrets) throws HeadlessException {
		this(new FretboardLayout(numberOfStrings, numberOfFrets, FretboardStyle.STANDARD));
	}

	InteractiveFretboard(FretboardLayout layout) {
		super("Interactive fretboard");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.layout = layout;
		int numberOfStrings = layout.getNumberOfStrings();
		int numberOfFrets = layout.getNumberOfFrets();
		this.setLayout(new GridLayout(numberOfFrets + 2, numberOfStrings, GRID_LAYOUT_GAP, GRID_LAYOUT_GAP));
		// Assemble the Fretboard:
		this.strings = new FretHandler[numberOfStrings];
		FretValueDisplayLabel newLabel;
		// Add labels at top:
		for (int i = 0; i < numberOfStrings; i++) {
			newLabel = new FretValueDisplayLabel();
			this.strings[i] = new FretHandler(numberOfFrets);
			this.strings[i].addObserverAndUpdate(newLabel);
			this.add(newLabel);
		}
		// Add buttons:
		
		// TODO: HERE
		// HERE
		// Too much egg nog
		
		FretButton newButton;
		int fretNumber, stringNumber, numberOfButtons;
		numberOfButtons = numberOfStrings * (numberOfFrets + 1);
		for (int i = 0; i < numberOfButtons; i++) {
			fretNumber = i / numberOfStrings;
			stringNumber = i % numberOfStrings;
			if (fretNumber == 0) {
				newButton = new FretButton(fretNumber, this.strings[stringNumber], FretButton.FretButtonType.BAR);
			} else {
				newButton = new FretButton(fretNumber, this.strings[stringNumber], FretButton.FretButtonType.REGULAR);
			}
			this.strings[stringNumber].addFretButton(newButton);
			this.add(newButton);
		}
		// Finish and show frame:
		this.pack();
		this.setVisible(true);

	}

	public static void main(String[] args) {
		new InteractiveFretboard();
	}
}
