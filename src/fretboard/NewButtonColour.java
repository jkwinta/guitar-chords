package fretboard;

import java.awt.Color;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;

import javax.imageio.ImageIO;

public class NewButtonColour {

	public NewButtonColour() {
		// TODO Auto-generated constructor stub
	}
	
	public static int[] rgbToArray(int rgb){
		int [] result = new int[3];
		result[0] = (rgb >> 16) & 0xFFFF;
		result[1] = (rgb >> 8) & 0xFFFF;
		result[2] = rgb & 0xFFFF;
		return result;
	}

	static void recolourButton() {
	}

	public static void main(String[] args) {
		File f = new File("./fret_icons/png/bar_roll.png");
		BufferedImage im = null;
		try {
			im = ImageIO.read(f);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
//		System.out.println(im.getClass());
		int nextNum = 0;
		int rgb = -1;
		int value = -1;
		HashMap<Integer,Integer> valMap = new HashMap<Integer, Integer>();
		for (int i = 0; i < im.getHeight(); i++){
			for (int j=0; j < im.getWidth(); j++){
				rgb = im.getRGB(j,i);
//				int [] rgbArray = rgbToArray(rgb);
//				System.out.print("(" + rgbArray[0]+"," + rgbArray[1]+"," + rgbArray[2] +")");
				System.out.print(new Color(rgb));
//				if (valMap.containsKey(rgb)){
//					value = valMap.get(rgb);
//				}else{
//					value = nextNum;
//					valMap.put(rgb, nextNum);
//					nextNum++;
//				}
//				if (value <10){
//					System.out.print(' ');
//				}
//				System.out.print(value);
//				System.out.print(' ');
			}
			System.out.println();
		}
//		System.out.println(valMap);
	}

}
