package fretboard;

import java.util.Observable;
import java.util.Observer;

import javax.swing.JLabel;
import javax.swing.SwingConstants;

@SuppressWarnings("serial") // No serialization, yet
public class FretValueDisplayLabel extends JLabel implements Observer {

	/**
	 * The String that gets displayed on the label for a string that is not
	 * fretted.
	 */
	static String UNFRETTED_STRING = "X";
	// static String UNFRETTED_STRING = "|";

	/**
	 * Public constructor for the FretValueDisplay, initially set to the
	 * unfretted character
	 */
	public FretValueDisplayLabel() {
		this(UNFRETTED_STRING);
	}

	/**
	 * Constructor called by the public constructor, just enforcing a centered
	 * text
	 * 
	 * @param text
	 *            The text to display (initially)
	 */
	private FretValueDisplayLabel(String text) {
		super(text, SwingConstants.CENTER);
	}

	/**
	 * Return a string of integer argument if it is a valid value for a fretted
	 * note or the String representing an unfretted note if it is not valid.
	 * 
	 * @param i
	 *            The number of the fret fretted.
	 * @return A String representing this fretted value.
	 */
	static String getDisplayString(int i) {
		if (i < 0) {
			return UNFRETTED_STRING;
		} else {
			return String.valueOf(i);
		}
	}

	/**
	 * Return a string of integer argument if it is a valid value for a fretted
	 * note on an instrument with numberOfFrets frets or the String representing
	 * an unfretted note if it is not valid.
	 * 
	 * @param i
	 *            The number of the fret fretted.
	 * @param numberOfFrets
	 *            The number of strings of the prospective instrument.
	 * @return A String representing this fretted value.
	 */
	static String getDisplayString(int i, int numberOfFrets) {
		if (i > numberOfFrets) {
			return UNFRETTED_STRING;
		} else {
			return getDisplayString(i);
		}
	}

	/**
	 * This will be the observer to a FretHandler, this will update this label
	 * to the FretHandler object's value fretted.
	 */
	@Override
	public void update(Observable o, Object arg) {
		if (o instanceof FretHandler) {
			FretHandler fh = (FretHandler) o;
			int fretted = fh.getFretted();
			this.setText(getDisplayString(fretted));
		}

	}

}
