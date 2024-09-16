package com.practice;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

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

    public void makeArrayStream(){
        String[] strArray = new String[]{
                "one", "two", "three", "four"
        };

        int[] intArray = new int[]{1,2,3,4,5};


        Stream<String> strStream = Arrays.stream(strArray);
        IntStream intStream = Arrays.stream(intArray);
    }

    public void makeCollectionsStream(){
        List<String> strList = List.of("one", "two", "three", "four");
        Set<Integer> intSet = Set.of(1,2,3,4,5);

        Stream<String> strStream = strList.stream();
        Stream<Integer> intStream = intSet.stream();

        System.out.println(intSet);
    }

    public void makeMapStream(){
        Map<String, Integer> map = Map.of(
                "0ne",1,"two",2,"three",3,"four",4,"five",5,
                "six",6,"seven",7,"eight",8,"nine",9,"ten",10
        );

        Stream<String> keyStream = map.keySet().stream();
        Stream<Integer> valueStream = map.values().stream();

        Stream<Map.Entry<String, Integer>> stream = map.entrySet().stream();
    }

    public void diffToListAndCollectors(){
        List<Integer> intList = List.of(1,2,3,4,5);

        List<Integer> intStream = intList.stream().toList();
        // 리스트 수정 시도 (불변 리스트이므로 예외 발생)
        try {
            intStream.add(6);  // UnsupportedOperationException 발생
        } catch (UnsupportedOperationException e) {
            System.out.println("intStream은 불변 리스트입니다. 요소를 추가할 수 없습니다.");
        }

        List<Integer> intList2 = List.of(1,2,3,4,5);
        List<Integer> intStream2 = intList2.stream().collect(Collectors.toList());
        intStream2.add(8);

        System.out.println("intStream2:"+intStream2);
    }

    public void convertToOtherDataStructure(){
        List<String> strList = List.of("one", "two", "three", "four");

        Set<Integer> strSet = strList.stream()
                .map(String::length)
                .collect(Collectors.toSet());

    }

    public void createSpecialStream(){
        int[] arr = new int[]{1,2,3,4,5,6};

        IntStream stream = Arrays.stream(arr);

        int sum = stream.sum();
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();
        double avg = Arrays.stream(arr).average().getAsDouble();

        System.out.println("sum = " + sum);
        System.out.println("min = " + min);
        System.out.println("max = " + max);
        System.out.println("avg = " + avg);
    }

    public void makeGroupingStreams(){
        List<String> strList = List.of("one", "two", "three", "four");

        Map<Integer, List<String>> grouping = strList.stream()
                .collect(Collectors.groupingBy(String::length));

        grouping.forEach((key, value) -> {
            System.out.println(key + ": " + value);
        });
    }


    public void convertBasicStream(){
        int[] arr = new int[]{1,2,3,4,5,6};

        List<Integer> collect = Arrays.stream(arr)
                .boxed()
                .collect(Collectors.toList());
    }

}
