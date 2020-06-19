// Totally untested, just some initla code to get started. 

package guessing_game;

public class Player {
	private String name; 
	private int lowGuess = 0;
	private int highGuess = 1000;
	private int lastGuess = (int) Math.random() * 1000;
	private int numGuesses = 0;
	
	public void setName(String str) {
		name = str;
	}
	
	public String getName() {
		return name ;
	}
	
	public int getGuess() {
		return lastGuess ;
	}
	
	public void setGuess(String highLow) {
		int high;
		int low;
		
		if (highLow == "high"){
		    high = lastGuess;
		    low = lowGuess;		
		} else {
			high = highGuess;
		    low = lastGuess;
		}
		lastGuess = (int)((high - low) / 2);		
	}

	public int getNumGuesses() {
		return numGuesses ;
	}
	
	public void setNumGuesses() {
		numGuesses += 1;
	}

}
