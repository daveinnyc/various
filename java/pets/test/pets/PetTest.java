/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pets;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author dave
 */
public class PetTest {
    
    public PetTest() {
    }
   
    /**
     * Test of sleep method, of class Pet.
     */
    @Test
    public void testSleep() {
        System.out.println("sleep");
        Pet instance = new Pet();
        instance.sleep();
        System.out.flush();
        // No return value to test
        
    }

    /**
     * Test of eat method, of class Pet.
     */
    @Test
    public void testEat() {
        System.out.println("eat");
        Pet instance = new Pet();
        instance.eat();
        System.out.flush();
        // No return value to test
    }

    /**
     * Test of talk method, of class Pet.
     */
    @Test
    public void testTalk() {
        System.out.println("talk");
        String aWord = "Woof";
        Pet instance = new Pet();
        String expResult = "Ok, ok Woof";
        String result = instance.talk(aWord);
        assertEquals(expResult, result);
    }
    
}
