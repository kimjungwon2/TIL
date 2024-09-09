package com.practice;

@Entity("MemberTable")
public class Member {
    private String name;
    private int age;

    public Member(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Member() {
    }

    public String getName(){
        return name;
    }

    public int getAge() {
        return age;
    }

    public void plusAge(int age){
        this.age = this.age + age;
    }

    private void minusAge(int age){
        this.age = this.age - age;
    }
}
