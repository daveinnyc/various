package cars;

/**
 * Exercise, 3.6 
 * @author dave
 */
public class CarOwner {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Car honda = new Car();
        
        System.out.println("honda");
        System.out.println(honda.start());
        System.out.println(honda.drive(10));
        System.out.println(honda.drive(0));
        System.out.println(honda.stop());

        System.out.println("\nlotus");
        Car lotus = new JamesBondCar();
        System.out.println(lotus.start());
        System.out.println(lotus.drive(10));
        System.out.println(lotus.drive(0));
        System.out.println(lotus.stop());       
    }    
}
