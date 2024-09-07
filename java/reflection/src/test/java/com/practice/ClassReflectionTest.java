package com.practice;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.lang.reflect.InvocationTargetException;

import static org.junit.jupiter.api.Assertions.*;

class ClassReflectionTest {

    @Test
    void getClassReflection() throws ClassNotFoundException {
        ClassReflection classReflection = new ClassReflection();
        classReflection.getClassReflection();
    }


    @Test
    void getConstructorReflection() throws InvocationTargetException, NoSuchMethodException, InstantiationException, IllegalAccessException {
        ClassReflection classReflection = new ClassReflection();

        classReflection.getConstructorByReflection();
    }

    @DisplayName("Field 획득하기")
    @Test
    void getFieldReflection() throws IllegalAccessException {
      //given
        ClassReflection classReflection = new ClassReflection();

      //when
        classReflection.getFieldReflection();
    }

    @DisplayName("Field 이름 변경하기")
    @Test
    void setNameFieldByReflection() throws IllegalAccessException, NoSuchFieldException {
        //given
        ClassReflection classReflection = new ClassReflection();

        //when
        classReflection.setNameFieldByReflection();
    }
}