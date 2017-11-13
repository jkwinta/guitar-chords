package fretboard;

import javax.swing.JLabel;

/**
 * A class that handles the array of fretButton objects that represent the
 * string of a stringed instrument, unfortunately, there is apparently already
 * a class called String.
 */
public class FretObserver {
	
	/**
	 * The String that gets displayed on the label for a string that is not
	 * fretted.
	 */
	static String UNFRETTED_STRING = "X";
	
	private FretButton[] frets;
	private JLabel displayLabel;
	private int fretted;
	private int fretsAdded;

	public FretObserver(int numberOfFrets, JLabel displayLabel) {
		this.fretsAdded = 0;
		this.fretted = -1;
		this.displayLabel = displayLabel;
		this.displayLabel.setText(UNFRETTED_STRING);
		this.frets = new FretButton[numberOfFrets];
	}
	
	void addFretButton(FretButton newFretButton){
		this.frets[this.fretsAdded] = newFretButton;
		this.fretsAdded++;
	}
	
	void fretButtonPress(int pressed){
		if (pressed == this.fretted){
			this.frets[this.fretted].unset();
			this.fretted = -1;
			this.displayLabel.setText(UNFRETTED_STRING);
		} else {
			this.frets[this.fretted].unset();
			this.frets[pressed].set();
			this.fretted = pressed;
			this.displayLabel.setText(String.valueOf(pressed));
		}
	}

}
