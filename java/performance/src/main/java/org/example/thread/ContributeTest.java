package org.example.thread;

public class ContributeTest {

    public static void main(String[] args) {
        Contributor[] crs = new Contributor[10];
        Contribution group = new Contribution();

        for(int loop=0;loop<10;loop++){

            crs[loop]=new Contributor(group," Contributor"+loop);
        }

        for(int loop=0;loop<10;loop++){
            crs[loop].start();
        }
    }
}
