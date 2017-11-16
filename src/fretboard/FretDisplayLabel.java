package fretboard;

import java.util.Observable;
import java.util.Observer;

import javax.swing.JLabel;
import javax.swing.SwingConstants;

@SuppressWarnings("serial") // No serialization, yet
public class FretDisplayLabel extends JLabel implements Observer {

	/**
	 * The String that gets displayed on the label for a string that is not
	 * fretted.
	 */
	static String UNFRETTED_STRING = "X";
	// static String UNFRETTED_STRING = "|";

	public FretDisplayLabel() {
		this(UNFRETTED_STRING);
	}

	private FretDisplayLabel(String text) {
		super(text, SwingConstants.CENTER);
	}

	static String getDisplayString(int i) {
		if (i < 0) {
			return UNFRETTED_STRING;
		} else {
			return String.valueOf(i);
		}
	}

	static String getDisplayString(int i, int numberOfFrets) {
		if (i > numberOfFrets) {
			return UNFRETTED_STRING;
		} else {
			return getDisplayString(i);
		}
	}

	@Override
	public void update(Observable o, Object arg) {
		if (o instanceof FretHandler) {
			FretHandler fh = (FretHandler) o;
			int fretted = fh.getFretted();
			this.setText(getDisplayString(fretted));
		}

	}

}
