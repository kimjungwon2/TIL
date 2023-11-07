package org.example.variable;

import java.io.FileReader;
import java.util.HashMap;

public class BadQueryManager {

    private static String queryURL = null;

    public BadQueryManager(String badUrl){
        queryURL= badUrl;
    }

    public static String getSql(String idSql){
        try{
        } catch(Exception ex){
            System.out.println(ex);
        }
        return null;
    }
}
