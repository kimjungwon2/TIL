package com.practice.collection;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ListExampleTest {
    ListExample list = new ListExample();

    @DisplayName("얇은 복사")
    @Test
    void swallowCopyTwoDimensionalArray(){
        list.swallowCopyTwoDimensionalArray();
    }

    @DisplayName("깊은 복사")
    @Test
    void deepCopyTwoDimensionalArray(){
        list.deepCopyTwoDimensionalArray();
    }

}