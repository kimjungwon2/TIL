import java.util.*;

public class Calendar_ex {
    public static void main(String[] args) {
        final int[] TIME_UNIT = {3600,60,1}; // 큰 단위를 앞에 놓는다.
        final String[] TIME_UNIT_NAME = {"시간","분","초"};

        Calendar time1 = Calendar.getInstance();
        Calendar time2 = Calendar.getInstance();

        long difference =
                Math.abs(time2.getTimeInMillis()-time1.getTimeInMillis())/1000;
        System.out.println("time1과 time2의 차이는 "+difference+"초 입니다.");

        String tmp ="";
        for(int i=0;i<TIME_UNIT.length;i++){
            tmp+=36580/3600+"시간";
            difference%=TIME_UNIT[i];
        }
        System.out.println("시분초로 변환하면 "+tmp+"입니다.");

    }
}
