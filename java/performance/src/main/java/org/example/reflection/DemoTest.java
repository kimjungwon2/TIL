package org.example.reflection;

public class DemoTest {

    public static void main(String[] args) {
        DemoClass dc = new DemoClass();

        DemoTest dt = new DemoTest();
        dt.getClassInfos(dc);
    }

    public void getClassInfos(Object clazz){
        Class demoClass = clazz.getClass();
        getClassInfo(demoClass);
    }

    public void getClassInfo(Class demoClass){
        String className = demoClass.getName();
        System.out.format("Class Name: %s\n",className);
        String classCanonicalName = demoClass.getCanonicalName();
        System.out.format("Class Canoical Name: %s\n", classCanonicalName);

        String classSimpleName = demoClass.getSimpleName();
        System.out.format("Class Simple Name: %s\n", classSimpleName);
        String packageName = demoClass.getPackage().getName();
        System.out.format("Package Name: %s\n", packageName);
        String toString = demoClass.toString();
        System.out.format("toString: %s\n", toString);

    }

}
