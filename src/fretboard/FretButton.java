package fretboard;

import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.BorderFactory;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;

import fretboard.FretIcons.FretIconStyle;

/**
 * A button as the atomic component of an interactive fretboard.
 * 
 * @author jkwinta
 *
 */
@SuppressWarnings("serial") // No need to serialize, at this point.
public class FretButton extends JButton {

	/**
	 * The fret number that this button represents, to send back to the parent
	 * when clicked.
	 */
	private int fretNumber;

	/**
	 * The parent that manages the collection of FretButton objects comprising a
	 * "string"
	 */
	private FretHandler stringParent;

	/**
	 * The icons to use for when a given note is fretted or not
	 */
	private ImageIcon frettedIcon, unfrettedIcon;

	/**
	 * The FretIconStyle that prescribes what icons to use
	 */
	private FretIconStyle style;

	/**
	 * Constructor for new FretButton from a number to pass and the parent to
	 * pass it to when clicked, and the style of images to use.
	 * 
	 * @param fretNumber
	 *            The fret number that this button represents, passed upon click
	 * @param stringParent
	 *            The parent that handles the string, to which the fretNumber is
	 *            passed on click
	 * @param style
	 *            The style that prescribes what icons to use
	 */
	FretButton(int fretNumber, FretHandler stringParent, FretIconStyle style) {
		super();
		this.fretNumber = fretNumber;
		this.stringParent = stringParent;
		this.style = style;
		Icon rollover;
		if (type == FretButtonType.BAR) {
			this.unfrettedIcon = BAR_STANDARD;
			this.frettedIcon = BAR_FRETTED;
			rollover = BAR_ROLLOVER;
		} else if (type == FretButtonType.LEFT_DOT) {
			this.unfrettedIcon = LEFT_DOT_STANDARD;
			this.frettedIcon = LEFT_DOT_FRETTED;
			rollover = LEFT_DOT_ROLLOVER;
		} else if (type == FretButtonType.RIGHT_DOT) {
			this.unfrettedIcon = RIGHT_DOT_STANDARD;
			this.frettedIcon = RIGHT_DOT_FRETTED;
			rollover = RIGHT_DOT_ROLLOVER;
		} else {
			this.unfrettedIcon = REGULAR_STANDARD;
			this.frettedIcon = REGULAR_FRETTED;
			rollover = REGULAR_ROLLOVER;
		}
		this.setRolloverIcon(rollover);
		this.setBorder(BorderFactory.createEmptyBorder());
		this.unset();
		this.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				Object source = e.getSource();
				if (source instanceof FretButton) {
					FretButton sourceFretButton = (FretButton) source;
					sourceFretButton.stringParent.fretButtonPress(sourceFretButton.fretNumber);
				}
			}
		});
	}

	/**
	 * Set the FretButton, showing it as the fretted note on its string.
	 */
	void set() {
		this.setIcon(this.frettedIcon);
		this.setRolloverEnabled(false);
	}

	/**
	 * Unset the FretButton, show it as no longer fretted on its string.
	 */
	void unset() {
		this.setIcon(this.unfrettedIcon);
		this.setRolloverEnabled(true);
		this.getModel().setRollover(false);
	}

	/**
	 * @return the FretIconStyle of this FretButton.
	 */
	public FretIconStyle getStyle() {
		return style;
	}

}
