package hello;

import hello.boot.MySpringApplication;
import hello.boot.MySpringBootApplication;
import org.apache.catalina.LifecycleException;

@MySpringBootApplication
public class MySpringBootMain {

    public static void main(String[] args) throws LifecycleException {
        System.out.println("MySpringBootMain.main");
        MySpringApplication.run(MySpringBootMain.class,  args);
    }
}
