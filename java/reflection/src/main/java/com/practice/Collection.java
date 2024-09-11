package com.practice;

import java.util.List;

public class Collection {

    public void iteratingCollectionsV1(){
        char[] array = new char[]{ 'h', 'e', 'l', 'l', 'o' };
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
        System.out.println();
    }

    public void iteratingCollectionsV2(){
        List<Character> list = List.of('h', 'e', 'l', 'l', 'o' );

        for(Character c: list){
            System.out.println(c);
        }
        System.out.println();
    }

    public void iteratingCollectionsV3(){
        List<Character> list = List.of('h', 'e', 'l', 'l', 'o' );

        list.stream().forEach(System.out::println);

        System.out.println();
    }
}
