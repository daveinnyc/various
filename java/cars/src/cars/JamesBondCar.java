package cars;

/**
 *
 * @author dave
 */
public class JamesBondCar extends Car {
    // Override base class method
     public int drive(int howLong){
        return howLong * 180;    
    }  
}
