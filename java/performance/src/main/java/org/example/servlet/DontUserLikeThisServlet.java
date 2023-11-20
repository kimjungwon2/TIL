package org.example.servlet;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class DontUserLikeThisServlet extends HttpServlet {

    private static final long serialVersionUID = 1L;
    String successFlag = "N";

    public DontUserLikeThisServlet(String successFlag) {
        super();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        successFlag = request.getParameter("successFlag");
    }

}
