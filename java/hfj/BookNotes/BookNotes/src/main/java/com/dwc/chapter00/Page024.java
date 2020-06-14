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
public class Page024 {
    public static void main(String[] arg){
        int x = 0;
        while ( x < 4 ){
        System.out.print("a");
        if ( x < 1 ){          
            System.out.print(" ");
        }
        System.out.print("n");
        if ( x > 1 ){
           System.out.print(" oyster");            
           x = x + 2;
        }     
        if ( x == 1 ){
           System.out.print("noys");
           }
        if ( x < 1 ){
           System.out.print("oise");
           }
        System.out.println("");
        x = x + 1;
        }
    }
}
