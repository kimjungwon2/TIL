package org.example.collection.list;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Vector;

public class ListAdd {

    int LOOP_COUNT = 1000;
    List<Integer> arrayList;
    List<Integer> vector;
    List<Integer> linkedList;

    public void addArrayList(){
        arrayList=  new ArrayList<Integer>();
        for(int loop=0;loop<LOOP_COUNT;loop++){
            arrayList.add(loop);
        }
    }

    public void addVector(){
        vector = new Vector<Integer>();
        for(int loop=0;loop<LOOP_COUNT;loop++){
            vector.add(loop);
        }
    }

    public void addLinkedList(){
        linkedList = new LinkedList<Integer>();
        for(int loop=0;loop<LOOP_COUNT;loop++){
            linkedList.add(loop);
        }
    }

}
