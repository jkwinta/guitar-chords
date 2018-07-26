package guitarchords;

import javax.swing.JFrame;

/**
 * An abstract JFrame that acts as an observable over a collection/array
 * representing the strings of a stringed instrument.
 * 
 * @author jkwinta
 *
 */
@SuppressWarnings("serial") // No serializing, yet
public abstract class FrettingChooser extends JFrame {

	private Chord chord;

	public FrettingChooser() {
		// TODO Auto-generated constructor stub
	}

	public FrettingChooser(String text) {
		super(text);
	}

	abstract public void updateFretting(int stringNumber, int newValue);

}
