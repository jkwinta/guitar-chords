package fretboard;

import java.awt.BorderLayout;
import java.awt.Dialog;
import java.awt.Frame;
import java.awt.GraphicsConfiguration;
import java.awt.Window;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.WindowConstants;

public class ExploreDialog extends JDialog {

	static final String title = "Explore what?";

	public ExploreDialog(Frame owner) {
		super(owner, title, true);
		JButton chordButton = new JButton("Chord");
		chordButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
			}
		});
		JButton scaleButton = new JButton("Scale");
		scaleButton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub

			}

		});
		JButton fretboardButton = new JButton("Interactive Fretboard");
		fretboardButton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub

			}

		});
		JPanel buttonPanel = new JPanel();
		buttonPanel.add(chordButton);
		buttonPanel.add(scaleButton);
		buttonPanel.add(fretboardButton);
		this.add(buttonPanel, BorderLayout.NORTH);

		JButton cancelButton = new JButton("Cancel");
		cancelButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				dispose();
			}
		});
		this.add(cancelButton, BorderLayout.SOUTH);
		this.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
		this.pack();
		this.setVisible(true);
	}

	public static void main(String args[]) {
		ExploreDialog a = new ExploreDialog(null);

	}

}
