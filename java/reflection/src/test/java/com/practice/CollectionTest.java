package com.practice;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CollectionTest {

    Collection collection = new Collection();

    @DisplayName("")
    @Test
    void testV1(){
        collection.iteratingCollectionsV1();
    }


    @DisplayName("")
    @Test
    void testV2(){
        collection.iteratingCollectionsV2();
    }

    @DisplayName("")
    @Test
    void testV3(){
        collection.iteratingCollectionsV3();
    }

    @DisplayName("")
    @Test
    void filterV1(){
      collection.filterAnimalV1();
    }

    @DisplayName("")
    @Test
    void filterV2(){
        collection.filterAnimalV2();
    }

    @DisplayName("")
    @Test
    void makeCollectionsStream(){
        collection.makeCollectionsStream();
    }

    @DisplayName("")
    @Test
    void diffToListAndCollectors(){
        collection.diffToListAndCollectors();
    }

    @DisplayName("")
    @Test
    void makeGrouping(){
      collection.makeGroupingStreams();
    }

}
