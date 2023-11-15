package org.example.io;

import java.io.BufferedReader;
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

    public static String readCharStreamWithBuffer(String fileName) throws Exception{
        StringBuffer retSB = new StringBuffer();
        FileReader fr = null;

        try{
            fr = new FileReader(fileName);
            int bufferSize = 1024*1024;
            char readBuffer[] = new char[bufferSize];
            int resultSize = 0;

            while((resultSize = fr.read(readBuffer))!=-1){
                if(resultSize==bufferSize){
                    retSB.append(readBuffer);
                } else{
                    for(int loop=0;loop<resultSize;loop++){
                        retSB.append(readBuffer[loop]);
                    }
                }
            }
            return retSB.toString();
        }catch(Exception e){
            e.printStackTrace();
        }

        return fileName;
    }

    public static ArrayList<String> readBufferedReader(String fileName) throws  Exception{
        ArrayList<String> list = new ArrayList<>();
        BufferedReader br = null;

        try{
            br = new BufferedReader(new FileReader(fileName));
            String data;
            while((data =br.readLine())!=null){
                list.add(data);
            }
        }catch(Exception e){
            System.out.println(e.getMessage());
            throw e;
        } finally{
            if(br!=null) br.close();
        }

        return list;
    }


    public static void main(String[] args) throws Exception{
        String fileName = "C:\\10MBFile";
    }
}
