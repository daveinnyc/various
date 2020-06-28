// Totally untested, just some initla code to get started. 

package guessing_game;

import java.util.*;


public class GuessingGame {
	// Maybe make this configurable at runtime later
	int numPlayers = 5;
	Player[] playerList = new Player[numPlayers]; 
	
	public void startGame() {
		// Create Players
		for(int p = 0; p < numPlayers ; p++) {
			Player newPlayer = new Player("Player" + Integer.toString(p));
			playerList[p] = newPlayer;
		}
		
		// Define target number
		int targetNumber = (int) (Math.random() * 1000);
        int winningPlayer = -1;
        int currentGuess = -1;
        boolean numberHasntBeenGuessedYet = true; 
        
		while(numberHasntBeenGuessedYet) {
			for( int i = 0; i < numPlayers ; i++) {
				playerList[i].incrementNumGuesses();
                currentGuess = playerList[i].getGuess();
                if (targetNumber == currentGuess) {
                	winningPlayer = i;
        			numberHasntBeenGuessedYet = false;
                } else if (targetNumber > currentGuess) {
                	playerList[i].setGuess("low");
                } else {
                	playerList[i].setGuess("high");
                }
			}	
		}
		
		// Report who won
    	System.out.println("Game Over");
    	System.out.print(playerList[winningPlayer].getName() + " guessed ");
    	System.out.print(Integer.toString(currentGuess));
    	System.out.print(" after "); 
    	System.out.print(Integer.toString(playerList[winningPlayer].getNumGuesses()));
    	System.out.println(" tries."); 
	}

}
