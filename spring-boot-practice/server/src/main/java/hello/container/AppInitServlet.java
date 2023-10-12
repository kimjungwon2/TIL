package hello.container;

import jakarta.servlet.ServletContext;

public class AppInitServlet implements AppInit{


    @Override
    public void onStartup(ServletContext servletContext) {
        System.out.println("AppInitV1Servlet.onStartup");
    }
}
