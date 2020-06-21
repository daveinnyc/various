// Totally untested, just some initla code to get started. 

package guessing_game;

import java.util.*;


public class GuessingGame {
	int numPlayers = 3;
	List<Player> playerList = new ArrayList<Player>(); 
	
	public void startGame() {
		System.out.println("Starting");
		// Create Players
		for(int p = 0; p < numPlayers ; p++) {
			Player newPlayer = new Player();
			newPlayer.setName("Player" + Integer.toString(p) ); 
			playerList.add(newPlayer);
		}
		
		// Define target number
		int targetNumber = (int) Math.random() * 1000;
        boolean numberHasntBeenGuessedYet = true; 
        
		// TODO Start guessing
		while(numberHasntBeenGuessedYet) {
			int numPlayers =  playerList.size();
			System.out.println("Num Players: " + numPlayers);
			
			
			System.out.println("Ending");
			numberHasntBeenGuessedYet = false;
		}
		// TODO Check if winner
		
		// TODO Report score
	}

}
