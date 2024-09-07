package com.practice;


import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;


public class ClassReflection {
    public void getClassReflection() throws ClassNotFoundException {
        Class<Member> aClass = Member.class;
        Member member1 = new Member("정원",25);
        Class<? extends Member> bClass = member1.getClass();
        Class<?> cClass = Class.forName("com.practice.Member");

        Field[] fields = aClass.getFields();
        Method[] methods = aClass.getMethods();
        Method[] declaredMethods = aClass.getDeclaredMethods();
        Field[] declaredFields = aClass.getDeclaredFields();

    }

    public void getConstructorByReflection() throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
        Class<Member> aClass = Member.class;
        Constructor<?> constructor = aClass.getDeclaredConstructor(String.class, int.class);
        Object object = constructor.newInstance("John Doe", 30);
        Member member = (Member) object;

    }

    public void getFieldReflection() throws IllegalAccessException {
        Class<Member> aClass = Member.class;
        Member member = new Member("정원", 30);

        for (Field field : aClass.getDeclaredFields()) {
            field.setAccessible(true);
            String fieldInfo = field.getType() + ", " + field.getName() + " = " + field.get(member);

            System.out.println("FieldInfo: " + fieldInfo);
        }
    }



}
