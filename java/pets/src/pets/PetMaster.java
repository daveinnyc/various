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
        
        Fish nemo = new Fish();
        nemo.dive(10);
        nemo.dive(15);
        System.out.println(nemo.dive(0));
        // Method is overwritten in Fish class
        System.out.println(nemo.talk("Hey Dori"));
        nemo.sleep();
        
    }    
}
