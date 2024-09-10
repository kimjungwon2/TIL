package com.practice;

import java.util.Arrays;

public class HelperClass {

    public void useArrays(){
        int[] nums = { 3, 5, 2, 4, 2, 9 };
        Arrays.sort(nums);

        for (int num : nums) {
            System.out.println(num);
        }
    }
}
