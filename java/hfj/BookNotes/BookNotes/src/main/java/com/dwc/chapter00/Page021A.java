/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.dwc.chapter00;

/**
 *
 * @author dave
 */
public class Page021A {
    public static void main(String[] arg){
        /* Orig had no decrement in loop, 
         * only ran below print threshold
         */
        int x = 5;
        while (x < 10){
            if (x > 3){
                System.out.println("Big X");
            }
        x -= 1;
        }
    }
    
}
