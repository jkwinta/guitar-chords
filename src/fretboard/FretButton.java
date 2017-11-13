package fretboard;

import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.Action;
import javax.swing.BorderFactory;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;

public class FretButton extends JButton {
	
	/*
	 * Return an ImageIcon read from the image file at path.
	 */
	static ImageIcon getImageIconFromFileString(String path) {
		File f = new File(path);
		Image im = null;
		try {
			im = ImageIO.read(f);
		} catch (IOException e) {
			System.out.println("Hey there buster, you're missing an icon file at " + path);
			System.exit(1);
		}
		return new ImageIcon(im);
	}

	// Paths to images that we may use:
	static final String BAR_STANDARD_PATH = "../fret_icons/png/bar.png";
//	static final String BAR_STANDARD_PATH = "../fret_icons/png/bar_x.png";
//	static final String BAR_STANDARD_PATH = "../fret_icons/png/bar_x_blue.png";
	static final String BAR_FRETTED_PATH = "../fret_icons/png/bar_fretted.png";
	static final String BAR_ROLLOVER_PATH = "../fret_icons/png/bar_roll.png";

	static final String REGULAR_STANDARD_PATH = "../fret_icons/png/reg.png";
	static final String REGULAR_FRETTED_PATH = "../fret_icons/png/reg_fretted.png";
	static final String REGULAR_ROLLOVER_PATH = "../fret_icons/png/reg_roll.png";

	static final String LEFT_DOT_STANDARD_PATH = "../fret_icons/png/left.png";
	static final String LEFT_DOT_FRETTED_PATH = "../fret_icons/png/left_fretted.png";
	static final String LEFT_DOT_ROLLOVER_PATH = "../fret_icons/png/left_roll.png";

	static final String RIGHT_DOT_STANDARD_PATH = "../fret_icons/png/right.png";
	static final String RIGHT_DOT_FRETTED_PATH = "../fret_icons/png/right_fretted.png";
	static final String RIGHT_DOT_ROLLOVER_PATH = "../fret_icons/png/right_roll.png";
	

	// The resulting ImageIcons:
	static final ImageIcon BAR_STANDARD = getImageIconFromFileString(BAR_STANDARD_PATH);
	static final ImageIcon BAR_FRETTED = getImageIconFromFileString(BAR_FRETTED_PATH);
	static final ImageIcon BAR_ROLLOVER = getImageIconFromFileString(BAR_ROLLOVER_PATH);

	static final ImageIcon REGULAR_STANDARD = getImageIconFromFileString(REGULAR_STANDARD_PATH);
	static final ImageIcon REGULAR_FRETTED = getImageIconFromFileString(REGULAR_FRETTED_PATH);
	static final ImageIcon REGULAR_ROLLOVER = getImageIconFromFileString(REGULAR_ROLLOVER_PATH);

	static final ImageIcon LEFT_DOT_STANDARD = getImageIconFromFileString(LEFT_DOT_STANDARD_PATH);
	static final ImageIcon LEFT_DOT_FRETTED = getImageIconFromFileString(LEFT_DOT_FRETTED_PATH);
	static final ImageIcon LEFT_DOT_ROLLOVER = getImageIconFromFileString(LEFT_DOT_ROLLOVER_PATH);

	static final ImageIcon RIGHT_DOT_STANDARD = getImageIconFromFileString(RIGHT_DOT_STANDARD_PATH);
	static final ImageIcon RIGHT_DOT_FRETTED = getImageIconFromFileString(RIGHT_DOT_FRETTED_PATH);
	static final ImageIcon RIGHT_DOT_ROLLOVER = getImageIconFromFileString(RIGHT_DOT_ROLLOVER_PATH);
	
	
	/*
	 * Each FretButton has a type that will prescribe what ImageIcon objects
	 * it will use.
	 */
	static enum FretButtonType {
		BAR, LEFT_DOT, RIGHT_DOT, REGULAR
	};
	
	private int fretNumber;
	private FretObserver stringParent;
	private ImageIcon frettedIcon, unfrettedIcon;
	private FretButtonType type;

	public FretButton(int fretNumber, FretObserver stringParent, FretButtonType type){
		super();
		this.fretNumber = fretNumber;
		this.stringParent = stringParent;
		this.type = type;
		Icon rollover;
		if (type == FretButtonType.BAR){
			this.unfrettedIcon = BAR_STANDARD;
			this.frettedIcon = BAR_FRETTED;
			rollover = BAR_ROLLOVER;
		} else if (type == FretButtonType.LEFT_DOT){
			this.unfrettedIcon = LEFT_DOT_STANDARD;
			this.frettedIcon = LEFT_DOT_FRETTED;
			rollover = LEFT_DOT_ROLLOVER;
		} else if (type == FretButtonType.RIGHT_DOT){
			this.unfrettedIcon = RIGHT_DOT_STANDARD;
			this.frettedIcon = RIGHT_DOT_FRETTED;
			rollover = RIGHT_DOT_ROLLOVER;
		} else{
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
				// TODO WHAT DOES THE BUTTON DO????
				Object source = e.getSource();
				if (source instanceof FretButton){
					FretButton sourceFretButton = (FretButton) source;
					sourceFretButton.stringParent.fretButtonPress(sourceFretButton.fretNumber);
				}
			}
		});
	}
	
	void set(){
		this.setIcon(this.frettedIcon);
		this.setRolloverEnabled(false);
	}
	
	void unset(){
		this.setIcon(this.unfrettedIcon);
		this.setRolloverEnabled(true);
	}
	
}
