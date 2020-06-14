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
public class Page020 {
    public static void main(String[] args) {
        int x = 3;
        if (x == 3){
           System.out.print("a");
        }
        while (x > 0){
            x = x - 1;
            System.out.print("-");
            if (x == 1){
                System.out.print("d");
                x = x - 1;
            }           
            if (x == 2){
               System.out.print("b c");
            } 
        }
    }
}
