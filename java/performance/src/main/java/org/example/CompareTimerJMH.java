package org.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public class CompareTimerJMH {

    @GenerateMicroBenchmark
    public DummyData makeObject(){
        HashMap<String, String> map = new HashMap<>(1000000);
        ArrayList<String> list = new ArrayList<>(1000000);
        return new DummyData(map,list);
    }

}
