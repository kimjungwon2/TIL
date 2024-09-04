package com.practice;


public class ClassReflection {
    public void getClassReflection() throws ClassNotFoundException {
        Class<Member> aClass = Member.class;
        Member member1 = new Member();
        Class<? extends Member> bClass = member1.getClass();
        Class<?> cClass = Class.forName("com.practice.Member");
    }
}
