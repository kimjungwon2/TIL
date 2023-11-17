package org.example.log;



public class StringFormat {

    String a = "aaa", b="bbb", c="ccc";
    long d=1,e=2,f=3;

    String data;

    public void timeStringAdd(int repeats){
        for(int reps=0;reps<repeats;reps++){
            data = a+" "+b+" "+c+" "+d+" "+e+" "+f;
        }
    }

    public void timeFormat(int repeats){
        for(int reps= 0; reps<repeats;reps++){
            data = String.format("%s %s %s %d %d %d",a,b,c,d,e,f);
        }
    }

}
