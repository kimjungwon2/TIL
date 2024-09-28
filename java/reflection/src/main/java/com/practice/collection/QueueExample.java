package com.practice.collection;

import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {

    public void useQueue(){
        Queue<Integer> queue = new ArrayDeque<Integer>();

        queue.add(1);
        queue.add(2);
        queue.add(3);
        System.out.println(queue);

        Integer peek = queue.peek();
        System.out.println(peek);

        queue.remove();
        System.out.println(queue);

        boolean empty = queue.isEmpty();
        System.out.println(empty);
    }


}
