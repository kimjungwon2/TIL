package hello.container;

import hello.servlet.HelloServlet;
import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletRegistration.Dynamic;

public class AppInitServlet implements AppInit{


    @Override
    public void onStartup(ServletContext servletContext) {
        System.out.println("AppInitV1Servlet.onStartup");

        Dynamic helloServlet = servletContext.addServlet("helloServlet", new HelloServlet());

        helloServlet.addMapping("/hello-servlet");


    }
}
