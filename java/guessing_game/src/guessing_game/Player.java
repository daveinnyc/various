// Totally untested, just some initla code to get started. 

package guessing_game;

public class Player {
	private String name; 
	private int lowGuess;
	private int highGuess;
	private int currentGuess;
	private int numGuesses;
	
	
	public Player(String name){
		this.name = name; 
		this.lowGuess = 0;
		this.highGuess = 1000;
		this.currentGuess = (int) (Math.random() * 1000);
		this.numGuesses = 0;
			
	}
	
	public void setName(String str) {
		this.name = str;
	}
	
	public String getName() {
		return this.name ;
	}
	
	public int getGuess() {
		return this.currentGuess ;
	}
	
	public void setGuess(String highLow) {
		if (highLow == "high"){
			// Guess was higher than the target
			this.highGuess = this.currentGuess;
			this.currentGuess = this.lowGuess + (int)((this.currentGuess - this.lowGuess) / 2) ;
		} else if (highLow == "low"){		
			// Guess was lower than the target
		    this.lowGuess = this.currentGuess;
			this.currentGuess = this.lowGuess + (int)((this.highGuess - this.lowGuess) / 2) ;		
		} else {
			System.out.println("ERROR: needs 'high' or 'low'");
		}
		
		
	}

	public int getNumGuesses() {
		return numGuesses ;
	}
	
	public void incrementNumGuesses() {
		numGuesses += 1;
	}

}
