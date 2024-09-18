package com.practice;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class StringExampleTest {
    StringExample stringExample = new StringExample();
    @Test
    void getCharAt() {

        stringExample.getCharAt();
    }

    @Test
    void getSubstring() {
        stringExample.doSubstring();
    }
}