package fretboard;

import javax.swing.JLabel;

/**
 * A class that handles the array of fretButton objects that represent the
 * string of a stringed instrument, unfortunately, there is apparently already a
 * class called String. Called FretObserver, as a nod to the design pattern that
 * this vaguely suggests/mimics.
 * 
 * @author jkwinta
 */
public class FretObserver {

	/**
	 * The String that gets displayed on the label for a string that is not
	 * fretted.
	 */
	static String UNFRETTED_STRING = "X";
	// static String UNFRETTED_STRING = "|";

	/** Array of FretButton objects that this FretObserver is in charge of */
	private FretButton[] frets;

	/** JLabel to display the value `fretted' at this FretObserver (string) */
	private JLabel displayLabel;

	/**
	 * The value of fret held on the string of this FretObserver, -1, for
	 * unfretted
	 */
	private int fretted;

	/**
	 * Index for keeping track of where to add the next FretButton when
	 * initially assembling
	 */
	private int fretsAdded;

	/**
	 * Constructor for FretObserver taking the number of frets (FretButton
	 * objects) that will be added, and the JLabel where it can display its
	 * value.
	 * 
	 * @param numberOfFrets
	 *            The number of FretButton objects (less one for the open
	 *            string) that this FretObserver will observe, control, and
	 *            handle input from.
	 * @param displayLabel
	 *            The JLabel for displaying the value of this FretObserver.
	 */
	FretObserver(int numberOfFrets, JLabel displayLabel) {
		this.fretsAdded = 0;
		this.fretted = -1;
		this.displayLabel = displayLabel;
		this.displayLabel.setText(UNFRETTED_STRING);
		this.frets = new FretButton[numberOfFrets + 1];
	}

	/**
	 * Return the number of frets that this FretObserver represents. This is 1
	 * fewer than the number of FretButtons watched, as there is a button for
	 * the empty (unfretted) string note.
	 * 
	 * @return The number of frets this FretObserver represents.
	 */
	int getNumberOfFrets() {
		return this.frets.length - 1;
	}

	/**
	 * Return true if there is room in this FretObserver object to add another
	 * FretButton, false otherwise.
	 * 
	 * @return Whether or not a FretButton can be added.
	 */
	boolean hasRoom() {
		return this.fretsAdded <= this.getNumberOfFrets();
	}

	/**
	 * Add newFretButton to this FretObserver object's array of them in the next
	 * available index. The FretButton should have this FretObserver as its
	 * stringParent.
	 * 
	 * @param newFretButton
	 *            The FretButton to be added.
	 */
	void addFretButton(FretButton newFretButton) {
		this.frets[this.fretsAdded] = newFretButton;
		this.fretsAdded++;
	}

	/**
	 * Update the JLabel displayLabel to reflect the current value of fretted.
	 */
	void updateLabel() {
		if (this.fretted == -1) {
			this.displayLabel.setText(UNFRETTED_STRING);
		} else {
			this.displayLabel.setText(String.valueOf(this.fretted));
		}
	}

	/**
	 * Handles the pressing of a FretButton for which this FretObserver is the
	 * stringParent.
	 * 
	 * @param pressed
	 */
	void fretButtonPress(int pressed) {
		if (pressed == this.fretted) {
			this.setFretted(-1);
		} else {
			this.setFretted(pressed);
		}
	}

	/**
	 * Set the note given by toFret to be fretted. Do nothing if the value is
	 * invalid.
	 * 
	 * @param toFret
	 *            The value to set fretted. Should be between -1 and
	 *            getNumberOfFrets()
	 */
	void setFretted(int toFret) {
		if (toFret < -1 || toFret > this.getNumberOfFrets()) {
			return;
		} else if (this.fretted == toFret) {
			return;
		} else {
			if (this.fretted != -1) {
				this.frets[this.fretted].unset();
			}
			this.fretted = toFret;
			if (toFret != -1) {
				this.frets[this.fretted].set();
			}
		}
		this.updateLabel();
	}

	/**
	 * Return the value fretted represented in this FretObserver.
	 * 
	 * @return the value fretted, -1 if there is not a fretted note.
	 */
	public int getFretted() {
		return this.fretted;
	}

}
