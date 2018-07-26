package fretboard;

import java.util.Observable;
import java.util.Observer;

/**
 * A class that handles the input on the array of fretButton objects that
 * represent the string of a stringed instrument. Unfortunately, there was
 * apparently already a class called String.
 * 
 * @author jkwinta
 */
public class FretHandler extends Observable {

	/** Array of FretButton objects that this FretHandler is in charge of */
	private FretButton[] frets;

	/**
	 * The value of fret held on the string of this FretHandler, -1, for
	 * unfretted
	 */
	private int fretted;

	/**
	 * Index for keeping track of where to add the next FretButton when
	 * initially assembling
	 */
	private int fretsAdded;

	/**
	 * Constructor for FretHandler taking the number of frets (FretButton
	 * objects) that will be added.
	 * 
	 * @param numberOfFrets
	 *            The number of FretButton objects (less one for the open
	 *            string) that this FretHandler will observe, control, and
	 *            handle input from.
	 */
	FretHandler(int numberOfFrets) {
		this.fretsAdded = 0;
		this.fretted = -1;
		this.frets = new FretButton[numberOfFrets + 1];
	}

	public void addObserverAndUpdate(Observer o) {
		this.addObserver(o);
		o.update(this, null);
	}

	/**
	 * Return the number of frets that this FretHandler represents. This is 1
	 * fewer than the number of FretButtons watched, as there is a button for
	 * the empty (unfretted) string note.
	 * 
	 * @return The number of frets this FretHandler represents.
	 */
	int getNumberOfFrets() {
		return this.frets.length - 1;
	}

	/**
	 * Return true if there is room in this FretHandler object to add another
	 * FretButton, false otherwise.
	 * 
	 * @return Whether or not a FretButton can be added.
	 */
	boolean hasRoom() {
		// Note: LESS THAN OR EQUAL accounted for open string, fretted = 0.
		return this.fretsAdded <= this.getNumberOfFrets();
	}

	/**
	 * Add newFretButton to this FretHandler object's array of them in the next
	 * available index. The FretButton should have this FretHandler as its
	 * stringParent.
	 * 
	 * @param newFretButton
	 *            The FretButton to be added.
	 */
	void addFretButton(FretButton newFretButton) {
		this.frets[this.fretsAdded] = newFretButton;
		this.fretsAdded++;
	}

	// /**
	// * Update the JLabel displayLabel to reflect the current value of fretted.
	// */
	// void updateLabel() {
	// if (this.fretted == -1) {
	// this.displayLabel.setText(UNFRETTED_STRING);
	// } else {
	// this.displayLabel.setText(String.valueOf(this.fretted));
	// }
	// }

	/**
	 * Handles the pressing of a FretButton for which this FretHandler is the
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
		this.setChanged();
		this.notifyObservers();
	}

	/**
	 * Return the value fretted represented in this FretHandler.
	 * 
	 * @return the value fretted, -1 if there is not a fretted note.
	 */
	public int getFretted() {
		return this.fretted;
	}

}
