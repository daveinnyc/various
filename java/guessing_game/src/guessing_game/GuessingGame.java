package guessing_game;

import java.util.*;


public class GuessingGame {
	int numPlayers = 3;
	List<Player> playerList = new ArrayList<Player>(); 
	
	public void StartGame() {
		// Create Players
		for(int p = 0; p < numPlayers ; p++) {
			Player newPlayer = new Player();
			newPlayer.setName("Player" + Integer.toString(p) ); 
			playerList.add(newPlayer);
		}
		
		// TODO Define target number
		
		// TODO Start guessing
		
		// TODO Check if winner
		
		// TODO Report score
	}

}
