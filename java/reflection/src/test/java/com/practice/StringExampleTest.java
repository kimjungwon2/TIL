package com.practice;

import org.junit.jupiter.api.DisplayName;
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

    @DisplayName("")
    @Test
    void contain(){
        stringExample.contain();
    }

    @DisplayName("")
    @Test
    void split(){
        stringExample.split();
    }

    @DisplayName("")
    @Test
    void trim(){
        stringExample.trim();
    }

    @DisplayName("")
    @Test
    void test(){
      stringExample.doStringBuilder();
    }


}