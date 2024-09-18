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

    public void doSubstring(){
        String str = "banana";
        String substring = str.substring(1, 4);
        System.out.println(substring);
    }

    public void contain(){
        String str = "banana";
        boolean isContains = str.contains("ab");
        System.out.println(isContains);
    }

    public void split(){
        String str = "Hello my name is jungwon";
        String[] words = str.split(" ");

        for(String word: words){
            System.out.println(word);
        }

    }


    public void trim(){
        String message = " Hi banana i'm jungwon\n";

        String trimmed = message.trim();
        System.out.println(message);
        System.out.println(trimmed);
    }
}
