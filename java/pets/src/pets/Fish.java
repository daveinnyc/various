package pets;

/**
 *
 * @author dave
 */
public class Fish extends Pet{
   int currentDepth = 0;
   
   public int dive(int howDeep){
       currentDepth = currentDepth + howDeep;
       System.out.println("Diving " + howDeep + " feet");
       System.out.println("Current depth: " + currentDepth);
       
       return currentDepth;
   }
   
   public String talk(String someText){
       // Overrides pet.talk()
       return ("Fish don\'t talk");
   }
}
