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
            FileReader reader = new FileReader(idSql);
            HashMap<String,String> document = reader.read(queryURL);
            return document.get(idSql);
        } catch(Exception ex){
            System.out.println(ex);
        }
        return null;
    }
}
