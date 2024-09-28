package com.practice.collection;

import java.util.ArrayDeque;
import java.util.Deque;
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

    public void useStack(){
        Deque<Integer> s = new ArrayDeque<>();

        s.push(1);
        s.push(2);
        s.push(3);
        System.out.println(s);

        s.pop();
        s.pop();
        System.out.println(s);

        boolean empty = s.isEmpty();

        System.out.println(empty);
    }
}
