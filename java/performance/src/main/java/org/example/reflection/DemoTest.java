package org.example.reflection;

import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

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

    private void getMethodInfo(Class demoClass){
        System.out.println("----------------");
        Method[] method1 = demoClass.getDeclaredMethods();
        Method[] method2 = demoClass.getMethods();
        System.out.format("Declared methods: %d, Methods: %d\n", method1.length,method2.length);

        for(Method met1: method1) {
            String methodName = met1.getName();
            int modifier = met1.getModifiers();
            String modifierStr = Modifier.toString(modifier);
            String returnType = met1.getReturnType().getSimpleName();
            Class params[] = met1.getParameterTypes();
            StringBuilder paramStr = new StringBuilder();
            int paramLen = params.length;

            if (paramLen != 0) {
                paramStr.append(params[0].getSimpleName()).append(" arg");
                for (int loop = 1; loop < paramLen; loop++) {
                    paramStr.append(",").append(params[loop].getName())
                            .append(" arg").append(loop);
                }
            }

            Class exceptions[] = met1.getExceptionTypes();
            StringBuilder exceptionStr = new StringBuilder();
            int exceptionLen = exceptions.length;

            if (exceptionLen != 0) {
                exceptionStr.append("throws")
                        .append(exceptions[0].getSimpleName());

                for (int loop = 1; loop < exceptionLen; loop++) {
                    exceptionStr.append(",")
                            .append(exceptions[loop].getSimpleName());
                }

                System.out.format("%s %s %s(%s) %s\n", modifierStr, returnType,
                        methodName, paramStr, exceptionStr);
            }
        }
    }

}
