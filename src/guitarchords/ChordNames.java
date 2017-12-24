package guitarchords;

import java.util.HashMap;

public class ChordNames {

	private static HashMap<String, int[]> chordList;

	public ChordNames() {
		// TODO Auto-generated constructor stub
	}

	String[] degreeNames = { "R/root", // 0
			"2-/min2", // 1
			"2+/maj2", // 2
			"3-/min3", // 3
			"3+/maj3", // 4
			"4/4p/perf4", // 5
			"4a/aug4/dim5/5d/tri", // 6
			"5/5p/perf5", // 7
			"6-/min6", // 8
			"6+/maj6", // 9
			"7-/min7", // 10
			"7+/maj7" };// 11

	// d = {'maj': ('R', '3+', '5P'),
	// 'min': ('R', '3-', '5P'),
	// 'aug': ('R', '3+', '6-'),
	// 'dim': ('R', '3-', '4A/5D'),
	// ####
	// '7': ('R', '3+', '5P', '7-'),
	// 'dim7': ('R', '3-', '4A/5D', '6+'),
	// 'halfdim7': ('R', '3-', '4A/5D', '7-'),
	// 'min7': ('R', '3-', '5P', '7-'),
	// 'minmaj7': ('R', '3-', '5P', '7+'),
	// 'maj7': ('R', '3+', '5P', '7+'),
	// 'aug7': ('R', '3+', '6-', '7-'),
	// 'augmaj7': ('R', '3+', '6-', '7+')
	// }
}
