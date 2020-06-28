// Totally untested, just some initla code to get started. 

package guessing_game;

public class Player {
	private String name; 
	private int lowGuess;
	private int highGuess;
	private int lastGuess;
	private int numGuesses;
	
	
	public Player(String name){
		this.name = name; 
		this.lowGuess = 0;
		this.highGuess = 1000;
		this.lastGuess = (int) (Math.random() * 1000);
		this.numGuesses = 0;
			
	}
	
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
