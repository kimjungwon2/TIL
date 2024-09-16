package com.practice.collection;

import java.util.Arrays;

public class ListExample {

    public void createFixedArray(){
        int[] arr = new int[10];
        String[] stringArray = new String[10];

        char[] charArray = {'h','e','l','l','o'};


        System.out.println(arr[3]);
        System.out.println(arr[arr.length-1]);
    }

    public void copyStaticArray(){
        int[] arr = {1,2,3,4,5};
        int[] copy1 = Arrays.copyOf(arr, arr.length);
        int[] copy2 = Arrays.copyOfRange(arr, 1, 3);


        System.out.println(copy1);
        System.out.println(copy2);
    }
}
