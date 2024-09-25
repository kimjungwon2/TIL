package com.practice.collection;

import java.util.ArrayList;
import java.util.List;

public class DynamicArray {

    public void basicFunction(){
        List<Integer> list = new ArrayList<>(List.of(1,2,3,4,5));

        Integer i = list.get(3);
        System.out.println(i);

        list.set(4,100);
        System.out.println(list);

        list.add(100);
        System.out.println(list);

        list.add(2, 10);
        System.out.println(list);

        list.remove(list.size()-1);
        System.out.println(list);

        list.remove(2);

        System.out.println(list);
    }

}
