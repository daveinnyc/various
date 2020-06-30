package chapter03;

public class HobbitsTestDrive {
	public static void main(String[] args) {
		int numHobbits = 3;
		Hobbits[] h = new Hobbits[numHobbits];

		int i = 0;
		while (i < numHobbits) {
			h[i] = new Hobbits();
			if (i == 0) {
				h[i].name = "Bilbo";
			} else if (i == 1) {
				h[i].name = "Frodo";
			} else if (i == 2) {
				h[i].name = "Sam";
			} else {
				System.out.println("Unknown Hobbit");
			}
		
 	        System.out.println(h[i].name + " is a good Hobbit name.");
			i++;	    
		}
	}
}
