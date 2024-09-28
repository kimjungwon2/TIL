package com.practice.collection;

import java.util.LinkedList;
import java.util.List;

public class LinkedListExample {

    public void useLinkedList(){

        LinkedList<String> linkedList = new LinkedList<>();

        linkedList.add("Apple");
        linkedList.add("Banana");
        linkedList.add("Cherry");
        System.out.println("Initial LinkedList: " + linkedList);


        linkedList.addFirst("Mango");
        System.out.println("After addFirst: " + linkedList);


        linkedList.addLast("Orange");
        System.out.println("After addLast: " + linkedList);


        linkedList.add(2, "Grapes");
        System.out.println("After adding element at index 2: " + linkedList);


        String firstElement = linkedList.getFirst();
        System.out.println("First element: " + firstElement);


        String lastElement = linkedList.getLast();
        System.out.println("Last element: " + lastElement);

        linkedList.remove("Banana");
        System.out.println("After removing 'Banana': " + linkedList);

        linkedList.removeFirst();
        System.out.println("After removing first element: " + linkedList);

        linkedList.removeLast();
        System.out.println("After removing last element: " + linkedList);

        linkedList.remove(1);
        System.out.println("After removing element at index 1: " + linkedList);

        boolean isEmpty = linkedList.isEmpty();
        System.out.println("Is LinkedList empty? " + isEmpty);

        int size = linkedList.size();
        System.out.println("LinkedList size: " + size);

    }

}
