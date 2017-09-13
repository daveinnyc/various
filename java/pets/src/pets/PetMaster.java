package pets;

/**
 *
 * @author dave
 */
public class PetMaster {
    public static void main(String[] args){
        String petReaction;
        Pet budgie = new Pet();
        budgie.eat();
        petReaction = budgie.talk("Tweet Tweet");
        System.out.println(petReaction);
        budgie.sleep();
    }    
}
