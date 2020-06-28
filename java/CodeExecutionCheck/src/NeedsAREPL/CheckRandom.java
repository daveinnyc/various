package NeedsAREPL;

public class CheckRandom {
    public static void main(String[] args){
        int targetNumber = (int) (Math.random() * 1000);
            System.out.println("TARGET: " + Integer.toString(targetNumber));
    }
}
