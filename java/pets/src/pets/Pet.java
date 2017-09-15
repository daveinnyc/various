package pets;

/**
 *
 * @author dave
 */
public class Pet {
    int age;
    float weight;
    float height;
    String color;
    
    public static void sleep(){
        System.out.println("Good night");
    }
    
    public static void eat(){
        System.out.println("I'm hungry");
    }
    
    //public static String talk(String aWord){
    public String talk(String aWord){
        String response = "Ok, ok " + aWord;
        return response;
    }
}    
