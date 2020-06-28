// Totally untested, just some initla code to get started. 

package guessing_game;

import java.util.*;


public class GuessingGame {
	// Maybe make this configurable at runtime later
	int numPlayers = 3;
	Player[] playerList = new Player[numPlayers]; 
	
	public void startGame() {
		System.out.println("Starting");
		// Create Players
		for(int p = 0; p < numPlayers ; p++) {
			Player newPlayer = new Player("Player" + Integer.toString(p));
			playerList[p] = newPlayer;
		}
		
		// Define target number
		int targetNumber = (int) (Math.random() * 1000);
		System.out.println("TARGET: " + Integer.toString(targetNumber));
        boolean numberHasntBeenGuessedYet = true; 
        
		// TODO Start guessing
		while(numberHasntBeenGuessedYet) {
			for( int i = 0; i < numPlayers ; i++) {
                int currentGuess = playerList[i].getGuess();
                // is guess == actual
                 // if low
                 // if high
               System.out.println(currentGuess); 
			}
			
			
			System.out.println("Ending");
			numberHasntBeenGuessedYet = false;
		}
		// TODO Check if winner
		
		// TODO Report score
	}

}
