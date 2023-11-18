package org.example.log;

import java.util.ArrayList;

public class LogRemoveSample {

    private final boolean printFlag = false;
    public ArrayList getList(){
        ArrayList retList = new ArrayList(10);

        if(LogFlag.printFlag){
            System.out.format("LogRemoveSmaple.getList(): size=%d\n",retList.size());
        }
        return retList;
    }


}
