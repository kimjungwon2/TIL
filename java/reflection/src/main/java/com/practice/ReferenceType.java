package com.practice;

public class ReferenceType {
    public void referenceType(){
        int[] a = new int[]{1,2,3};

        int[] b = a;

        b[0] = 6;
        System.out.println("a[0] = " + a[0]);
        System.out.println("b[0] = " + b[0]);
        func(a);
        System.out.println("a[1] = " + a[1]);
    }

    public void referenceTypeForString() {
        String a = "안녕";
        String b = a;
        b = "완료";

        System.out.println("b = "+b);
        System.out.println("a = "+a);
    }

    public void referenceTypeForInteger() {
        Integer a = 1;
        Integer b = 3;
        b = 5;

        System.out.println("b = "+b);
        System.out.println("a = "+a);
    }


    private void func(int[] c){
        c[1] = 10;
        System.out.println("c[1] = " + c[1]);
    }


}
