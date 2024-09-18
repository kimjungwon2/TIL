package com.practice;

public class StringExample {

    public void replaceV1(){
        String old = "hello, world";
        old.replace('o','a');
        System.out.println("old = " + old);
    }

    public void replaceV2(){
        String old = "hello, world";
        String replaced = old.replace('o','a');

        System.out.println("replaced = " + replaced);
    }
}
