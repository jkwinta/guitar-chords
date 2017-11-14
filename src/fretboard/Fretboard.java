package fretboard;

import java.awt.GridLayout;
import java.awt.HeadlessException;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;

/**
 * The JFrame that handles building the interactive Fretboard.
 * 
 * @author jkwinta
 *
 */
@SuppressWarnings("serial") // Not serializing, quite yet
public class Fretboard extends JFrame {

	/**
	 * The gap between components in the GridLayout. Used for both horizontal
	 * and vertical gap values
	 */
	final static int GRID_LAYOUT_GAP = 0;

	/** The number of strings to use in the argument-less constructor. */
	final static int DEFAULT_NUMBER_OF_STRINGS = 6;

	/** The number of frets to use in the argument-less constructor. */
	final static int DEFAULT_NUMBER_OF_FRETS = 21;

	/** Array of FretObservers each representing instrument strings. */
	private FretObserver[] strings;

	/**
	 * Constructor for this Fretboard object.
	 * 
	 * @param numberOfStrings
	 * @param numberOfFrets
	 * @throws HeadlessException
	 */
	Fretboard(int numberOfStrings, int numberOfFrets) throws HeadlessException {
		super("Interactive fretboard");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLayout(new GridLayout(numberOfFrets + 2, numberOfStrings, GRID_LAYOUT_GAP, GRID_LAYOUT_GAP));
		// Assemble the Fretboard:
		this.strings = new FretObserver[numberOfStrings];
		JLabel newLabel;
		// Add labels at top:
		for (int i = 0; i < numberOfStrings; i++) {
			newLabel = new JLabel("", SwingConstants.CENTER);
			this.strings[i] = new FretObserver(numberOfFrets, newLabel);
			this.add(newLabel);
		}
		// Add buttons:
		FretButton newButton;
		int fretNumber, stringNumber, numberOfButtons;
		numberOfButtons = numberOfStrings * (numberOfFrets + 1);
		for (int i = 0; i < numberOfButtons; i++) {
			fretNumber = i / numberOfStrings;
			stringNumber = i % numberOfStrings;
			if (fretNumber == 0){
				newButton = new FretButton(fretNumber, this.strings[stringNumber], FretButton.FretButtonType.BAR);
			} else{
				newButton = new FretButton(fretNumber, this.strings[stringNumber], FretButton.FretButtonType.REGULAR);
			}
			this.strings[stringNumber].addFretButton(newButton);
			this.add(newButton);
		}
		// Finish and show frame:
		this.pack();
		this.setVisible(true);
	}

	Fretboard() throws HeadlessException {
		this(DEFAULT_NUMBER_OF_STRINGS, DEFAULT_NUMBER_OF_FRETS);
	}

	public static void main(String[] args) {
		new Fretboard();
	}
}
