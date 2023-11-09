package org.example.reflection;

import java.math.BigDecimal;

public class Reflection {

    int LOOP_COUNT = 1000;
    String result;

    public void withEquals(){
        Object src = new BigDecimal("6");
        for(int loop=0;loop<LOOP_COUNT;loop++){
            if(src.getClass().getName().equals("java.math.BigDecimal")){
                result = "BigDecimal";
            }
        }
    }

    public void withInstanceof(){
        Object src= new BigDecimal("6");
        for(int loop=0;loop<LOOP_COUNT;loop++){
            if(src instanceof java.math.BigDecimal){
                result = "BigDecimal";
            }
        }
    }
}
