package org.example.thread;

public class Contribution {

    private int amount = 0;
    public void donate(){
        amount++;
    }

    public int getTotal(){
        return amount;
    }

}
