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

    public void getLength(){
        String character = "Hello, world!";

        int length = character.length();

        System.out.println("length = " + length);
    }

    public void getCharAt(){
        String str = "banana";
        char c = str.charAt(2);
        System.out.println(c);
    }
}
