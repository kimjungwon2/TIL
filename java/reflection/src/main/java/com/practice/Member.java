package com.practice;

public class Member {
    private String name;
    private int age;

    public Member(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void getName(String name){
        this.name = name;
    }

    public void plusAge(int age){
        this.age = this.age + age;
    }

    private void minusAge(int age){
        this.age = this.age - age;
    }
}
