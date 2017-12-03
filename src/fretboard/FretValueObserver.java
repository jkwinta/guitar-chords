package fretboard;

import javax.swing.JLabel;
import javax.swing.SwingConstants;

/**
 * A class to handle storing the values of strings on the fretboard, mimicking
 * an observer pattern, but tailored better to the fact that we change (and thus
 * update) only one string at a time.
 * 
 * @author jkwinta
 *
 */
public class FretValueObserver {

	private int[] fretted;
	private JLabel[] labels;

	public FretValueObserver(int numberOfStrings, boolean hasLabels) {
		fretted = new int[numberOfStrings];
		if (hasLabels) {
			labels = new JLabel[numberOfStrings];
		} else {
			labels = null;
		}
		for (int i = 0; i < numberOfStrings; i++) {
			if (hasLabels){
				labels[i] = new JLabel("", SwingConstants.CENTER);
			}
			update(i, -1);
		}
	}

	void update(int stringIndex, int newFrettedValue) {
		fretted[stringIndex] = newFrettedValue;
		if (labels != null){
			labels[stringIndex].setText(String.valueOf(newFrettedValue));
		}
	}
	
	public static void main(String args[]){
		FretValueObserver a = new FretValueObserver(6, false);
		System.out.println(a.labels == null);
		System.out.println(a.labels != null);
		a = new FretValueObserver(6, true);
		System.out.println(a.labels == null);
		System.out.println(a.labels != null);
	}
}
