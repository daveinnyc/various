package cars;

/**
 *
 * @author dave
 */
public class Car {
    public String start(){
        return "Starting";
    }
    
    public String stop(){
        return "Stoping";
    }
    
    public int drive(int howLong){
        return howLong * 60;    
    }    
}
