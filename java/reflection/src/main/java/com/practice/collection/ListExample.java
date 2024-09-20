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

    public void swallowCopyTwoDimensionalArray(){
        int[][] arr = {{1,2,3},{4,5,6}};
        int[][] copy = Arrays.copyOf(arr, arr.length);

        copy[0][0] = 9999;

        System.out.println("arr[0][0] = "+arr[0][0]);
        System.out.println("copy[0][0] = "+copy[0][0]);
    }

    public void deepCopyTwoDimensionalArray(){
        int[][] arr = { {1, 2, 3}, {4, 5, 6} };
        int[][] copy = new int[arr.length][arr[0].length];
        for (int i = 0; i < arr.length; i++) {
            copy[i] = Arrays.copyOf(arr[i], arr[i].length);
        }
        copy[0][0] = 9999;
        System.out.println("arr[0][0] = "+arr[0][0]);
        System.out.println("copy[0][0] = "+copy[0][0]);
    }
}
