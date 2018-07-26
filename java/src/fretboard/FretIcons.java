package fretboard;

import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;

public class FretIcons {

	/**
	 * Return an ImageIcon read from the image file at path.
	 */
	private static ImageIcon getImageIconFromFileString(String path) {
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
	private static final String BAR_STANDARD_PATH = "./fret_icons/png/bar.png";
	// private static final String BAR_STANDARD_PATH =
	// "./fret_icons/png/bar_x.png";
	// private static final String BAR_STANDARD_PATH =
	// "./fret_icons/png/bar_x_blue.png";
	private static final String BAR_FRETTED_PATH = "./fret_icons/png/bar_fretted.png";
	private static final String BAR_ROLLOVER_PATH = "./fret_icons/png/bar_roll.png";

	private static final String REGULAR_STANDARD_PATH = "./fret_icons/png/reg.png";
	private static final String REGULAR_FRETTED_PATH = "./fret_icons/png/reg_fretted.png";
	private static final String REGULAR_ROLLOVER_PATH = "./fret_icons/png/reg_roll.png";

	private static final String LEFT_DOT_STANDARD_PATH = "./fret_icons/png/left.png";
	private static final String LEFT_DOT_FRETTED_PATH = "./fret_icons/png/left_fretted.png";
	private static final String LEFT_DOT_ROLLOVER_PATH = "./fret_icons/png/left_roll.png";

	private static final String RIGHT_DOT_STANDARD_PATH = "./fret_icons/png/right.png";
	private static final String RIGHT_DOT_FRETTED_PATH = "./fret_icons/png/right_fretted.png";
	private static final String RIGHT_DOT_ROLLOVER_PATH = "./fret_icons/png/right_roll.png";

	// The resulting ImageIcons:
	private static final ImageIcon BAR_STANDARD = getImageIconFromFileString(BAR_STANDARD_PATH);
	private static final ImageIcon BAR_FRETTED = getImageIconFromFileString(BAR_FRETTED_PATH);
	private static final ImageIcon BAR_ROLLOVER = getImageIconFromFileString(BAR_ROLLOVER_PATH);

	private static final ImageIcon REGULAR_STANDARD = getImageIconFromFileString(REGULAR_STANDARD_PATH);
	private static final ImageIcon REGULAR_FRETTED = getImageIconFromFileString(REGULAR_FRETTED_PATH);
	private static final ImageIcon REGULAR_ROLLOVER = getImageIconFromFileString(REGULAR_ROLLOVER_PATH);

	private static final ImageIcon LEFT_DOT_STANDARD = getImageIconFromFileString(LEFT_DOT_STANDARD_PATH);
	private static final ImageIcon LEFT_DOT_FRETTED = getImageIconFromFileString(LEFT_DOT_FRETTED_PATH);
	private static final ImageIcon LEFT_DOT_ROLLOVER = getImageIconFromFileString(LEFT_DOT_ROLLOVER_PATH);

	private static final ImageIcon RIGHT_DOT_STANDARD = getImageIconFromFileString(RIGHT_DOT_STANDARD_PATH);
	private static final ImageIcon RIGHT_DOT_FRETTED = getImageIconFromFileString(RIGHT_DOT_FRETTED_PATH);
	private static final ImageIcon RIGHT_DOT_ROLLOVER = getImageIconFromFileString(RIGHT_DOT_ROLLOVER_PATH);

	/**
	 * Each FretButton has a type that will prescribe what ImageIcon objects it
	 * will use.
	 */
	public static enum FretIconStyle {
		BAR, LEFT_DOT, RIGHT_DOT, REGULAR
	};

	/**
	 * Return the standard (unfretted) ImageIcon given a FretIconStyle
	 * 
	 * @param style
	 *            The FretIconStyle desired.
	 * @return The standard ImageIcon for FretIconStyle style.
	 */
	public static ImageIcon getStandardIcon(FretIconStyle style) {
		if (style == FretIconStyle.BAR) {
			return BAR_STANDARD;
		} else if (style == FretIconStyle.LEFT_DOT) {
			return LEFT_DOT_STANDARD;
		} else if (style == FretIconStyle.RIGHT_DOT) {
			return RIGHT_DOT_STANDARD;
		} else {
			return REGULAR_STANDARD;
		}
	}

	/**
	 * Return the fretted ImageIcon given a FretIconStyle
	 * 
	 * @param style
	 *            The FretIconStyle desired.
	 * @return The fretted ImageIcon for FretIconStyle style.
	 */
	public static ImageIcon getFrettedIcon(FretIconStyle style) {
		if (style == FretIconStyle.BAR) {
			return BAR_FRETTED;
		} else if (style == FretIconStyle.LEFT_DOT) {
			return LEFT_DOT_FRETTED;
		} else if (style == FretIconStyle.RIGHT_DOT) {
			return RIGHT_DOT_FRETTED;
		} else {
			return REGULAR_FRETTED;
		}
	}

	/**
	 * Return the rollover ImageIcon given a FretIconStyle
	 * 
	 * @param style
	 *            The FretIconStyle desired.
	 * @return The rollover ImageIcon for FretIconStyle style.
	 */
	public static ImageIcon getRolloverIcon(FretIconStyle style) {
		if (style == FretIconStyle.BAR) {
			return BAR_ROLLOVER;
		} else if (style == FretIconStyle.LEFT_DOT) {
			return LEFT_DOT_ROLLOVER;
		} else if (style == FretIconStyle.RIGHT_DOT) {
			return RIGHT_DOT_ROLLOVER;
		} else {
			return REGULAR_ROLLOVER;
		}
	}

	/*
	 * TODO: Something here should handle transparency or colour mapping if we
	 * wish to show frets as fractionally/conditionally fretted.
	 */

}
