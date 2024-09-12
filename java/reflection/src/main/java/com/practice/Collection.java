package com.practice;

import java.util.ArrayList;
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

    public void filterAnimalV1(){
        List<String> animals = List.of("rabbit", "tiger", "dog", "cat", "chicken");

        List<String> sorted = new ArrayList<>();
        for (String animal : animals) {
            if (animal.length() <= 3) continue;
            sorted.add(animal.toUpperCase());
        }
        sorted.sort(String::compareTo);
        for (int i = 0; i < 2; i++) {
            System.out.println(sorted.get(i));
        }
    }

    public void filterAnimalV2(){
        List<String> animals = List.of("rabbit", "tiger", "dog", "cat", "chicken");

        animals.stream()
                .filter(animal -> animal.length() > 3)
                .map(String::toUpperCase)
                .sorted()
                .limit(2)
                .forEach(System.out::println);
    }

}
