/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.dwc.booknotes;

/**
 *
 * @author dave
 */
public class p23 {
    public static void main(String[] arg){
        int x = 0;
        int y = 0;
        while (x < 5 ){
            x = x + 1;
            y = y + x;
            System.out.print(x + "" + y + " ");
            x = x + 1;
        }
    }
}
