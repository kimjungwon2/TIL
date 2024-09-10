package com.practice;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


class HelperClassTest {

    HelperClass helperClass = new HelperClass();

    @DisplayName("")
    @Test
    void useArrays(){
      helperClass.useArrays();
    }
}