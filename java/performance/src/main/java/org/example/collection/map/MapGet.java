package org.example.collection.map;

import java.util.HashMap;
import java.util.Hashtable;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;
import java.util.*;

public class MapGet {

    int LOOP_COUNT = 1000;
    Map<Integer, String> hashMap;
    Map<Integer, String> hashtable;
    Map<Integer, String> treeMap;
    Map<Integer, String> linkedHashMap;

    int keys[];

    public void setUp(){
        if(keys==null || keys.length!=LOOP_COUNT){
            hashMap=new HashMap<Integer,String>();
            hashtable = new Hashtable<Integer, String>();
            treeMap = new TreeMap<Integer, String>();
            linkedHashMap = new LinkedHashMap<Integer,String>();
            String data ="abcdefghijklmnopqrstuvwxyz";

            for(int loop=0;loop<LOOP_COUNT;loop++){
                String tempData = data+loop;
                hashMap.put(loop,tempData);
                hashtable.put(loop,tempData);
                treeMap.put(loop,tempData);
                linkedHashMap.put(loop,tempData);
            }

            keys = RandomKeyUtil.generateRandomNumberKeysSwap(LOOP_COUNT);

        }
    }

    public void getSeqHashMap(){
        for (int loop=0; loop<LOOP_COUNT;loop++) {
            hashMap.get(loop);
        }
    }

    public void getRandomHashMap(){
        for(int loop=0;loop<LOOP_COUNT;loop++){
            hashMap.get(keys[loop]);
        }
    }

    public void getSeqHashtable(){
        for(int loop=0;loop<LOOP_COUNT;loop++){
            hashtable.get(keys[loop]);
        }
    }

    public void getSeqHashTable(){
        for(int loop=0;loop<LOOP_COUNT;loop++){
            hashMap.get(keys[loop]);
        }
    }



}
