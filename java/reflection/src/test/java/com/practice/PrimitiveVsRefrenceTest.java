package com.practice;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class PrimitiveVsRefrenceTest {
    PrimitiveType primitiveType = new PrimitiveType();
    ReferenceType referenceType = new ReferenceType();

    @DisplayName("")
    @Test
    void executePrimitiveType(){
        primitiveType.primitiveType();
    }

    @DisplayName("")
    @Test
    void executeReferenceType(){
        referenceType.referenceType();
    }

    @DisplayName("")
    @Test
    void executeReferenceTypeForString(){
      //given
        referenceType.referenceTypeForString();

      //when

      //then
    }

}