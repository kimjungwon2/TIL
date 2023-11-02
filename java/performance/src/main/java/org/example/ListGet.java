package org.example;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Vector;

public class ListGet {

    int LOOP_COUNT = 1000;
    List<Integer> arrayList;
    List<Integer> vector;
    LinkedList<Integer> linkedList;

    int result = 0;

    public void setUp(){
        arrayList = new ArrayList<Integer>();
        vector = new Vector<Integer>();
        linkedList = new LinkedList<Integer>();

        for(int loop=0;loop<LOOP_COUNT;loop++){
            arrayList.add(loop);
            vector.add(loop);
            linkedList.add(loop);
        }
    }

    public void getArrayList(){
        for(int loop=0;loop<LOOP_COUNT;loop++){
            result = arrayList.get(loop);
        }
    }

    public void getVector(){
        for(int loop=0;loop<LOOP_COUNT;loop++){
            result = vector.get(loop);
        }
    }

    public void getLinkedList(){
        for(int loop=0;loop<LOOP_COUNT;loop++){
            result = linkedList.get(loop);
        }
    }


}
