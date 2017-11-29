package guitarchords;

public class Tunings {

	public Tunings() {
		// TODO Auto-generated constructor stub
	}

	static int[] STANDARD = getStandardTuning();

	private static int[] getStandardTuning() {
		int[] tuning = new int[6];
		tuning[1] = -3;
		tuning[0] = tuning[1] - 5;
		tuning[2] = tuning[1] + 5;
		tuning[3] = tuning[2] + 5;
		tuning[4] = tuning[3] + 4;
		tuning[5] = tuning[4] + 5;
		return tuning;
	}

}
