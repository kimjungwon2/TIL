package org.example.io;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class BasicIOReadUtil {

    public static ArrayList readCharStream(String fileName) throws Exception{
        ArrayList<StringBuffer> list = new ArrayList<StringBuffer>();
        FileReader fr = null;

        try{
            fr = new FileReader(fileName);
            int data = 0;

            StringBuffer sb = new StringBuffer();

            while((data=fr.read())!=-1){
                if(data=='\n'||data=='\r'){
                    list.add(sb);
                    sb.append((char)data);
                }else{
                    sb.append((char)data);
                }
            }
        } catch(IOException e){
            System.err.println(e.getMessage());
            throw e;
        } catch(Exception e){
            System.err.println(e.getMessage());
            throw e;
        } finally{
            if(fr!=null) fr.close();
        }
        return list;
    }

    public static void main(String[] args) throws Exception{
        String fileName = "C:\\10MBFile";
        StopWatch sw = new StopWatch();
        sw.start();
        ArrayList vlist1= BasicIOReadUtil.readCharStream(fileName);
        System.out.println(sw);
        System.out.println(list1.size());
    }
}
