package guitarchords;

import java.util.HashMap;

public class ChordNames {

	private static String INTERVAL_NAMES_SEP = "/";

	private static HashMap<String, int[]> chordList;

	public ChordNames() {
		// TODO Auto-generated constructor stub
	}

	private static String[] degreeNames = { "R/root", // 0
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

	private static HashMap<String, Integer> nameToInterval = makeNameToInterval();

	private static HashMap<String, Integer> makeNameToInterval() {
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		for (int i = 0; i < degreeNames.length; i++) {
			for (String name : degreeNames[i].split(INTERVAL_NAMES_SEP)) {
				map.put(name, i);
			}
		}
		return map;
	}

	public static String getIntervalName(int interval) {
		String[] names = degreeNames[interval % 12].split(INTERVAL_NAMES_SEP);
		return names[names.length - 1];
	}

	public static void main(String[] args) {
		for (int i = 0; i < ChordNames.degreeNames.length; i++) {
			System.out.println(ChordNames.degreeNames[i]);
		}
		System.out.println(ChordNames.nameToInterval);
		System.out.println(ChordNames.getIntervalName(7));
	}

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
