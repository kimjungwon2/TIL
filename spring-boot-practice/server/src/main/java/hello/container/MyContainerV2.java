package hello.container;

import jakarta.servlet.ServletContainerInitializer;
import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.HandlesTypes;
import java.util.Set;


@HandlesTypes(AppInit.class)
public class MyContainerV2 implements ServletContainerInitializer {

    @Override
    public void onStartup(Set<Class<?>> c, ServletContext ctx) throws ServletException {
        System.out.println("MyContainerV2.onStartup");
        System.out.println("MyContainerV2 c = "+c);
        System.out.println("MyContainerV2 ctx = "+ctx);
    }
}
