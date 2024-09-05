package com.practice;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ClassReflectionTest {

    @Test
    void getClassReflection() throws ClassNotFoundException {
        ClassReflection classReflection = new ClassReflection();
        classReflection.getClassReflection();
    }
}