package fretboard;

import javax.swing.BorderFactory;
import javax.swing.JLabel;

import fretboard.FretIcons.FretIconStyle;

@SuppressWarnings("serial") // No serializing quite yet.
public class FretLabel extends JLabel {
	// TODO : Check FretButton, this should be similar in construction.
	// Maybe deal with icon colour, etc. here??

	/**
	 * Constructor that calls the JLabel constructor with Icon argument of the
	 * standard (unfretted) Icon for the given FretIconStyle.
	 * 
	 * @param style
	 *            The FretIconStyle to use the standard Icon for.
	 */
	public FretLabel(FretIconStyle style) {
		super(FretIcons.getStandardIcon(style));
		this.setBorder(BorderFactory.createEmptyBorder());
	}
}
