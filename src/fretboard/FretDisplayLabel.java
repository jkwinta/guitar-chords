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

	public FretDisplayLabel(String text) {
		super(text, SwingConstants.CENTER);
	}

	@Override
	public void update(Observable o, Object arg) {
		if (o instanceof FretHandler) {
			FretHandler fh = (FretHandler) o;
			int fretted = fh.getFretted();
			if (fretted == -1) {
				this.setText(UNFRETTED_STRING);
			} else {
				this.setText(String.valueOf(fretted));
			}
		}

	}

}
