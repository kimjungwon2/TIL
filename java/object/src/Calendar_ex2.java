import java.util.Calendar;

public class Calendar_ex2 {
    public static void main(String[] args) {
        Calendar date =  Calendar.getInstance();
        date.set(2019,7,31);

        System.out.println(toString(date));

        System.out.println("= 1일 후 =");
        date.add(Calendar.DATE,1);
        System.out.println(toString(date));

        System.out.println("= 6달 전 =");
        date.add(Calendar.MONTH,-6);
        System.out.println(toString(date));

        //roll은 다른 필드에 영향을 안 준다.
        System.out.println("= 5달 전(roll) =");
        date.roll(Calendar.MONTH,-5);
        System.out.println(toString(date));

        System.out.println("= 6달 전 =");
        date.add(Calendar.DATE,31);
        System.out.println(toString(date));

    }

    public static String toString(Calendar date){
        return date.get(Calendar.YEAR)+"년 "+
                date.get(Calendar.MONTH)+"월 "+
                date.get(Calendar.DATE)+" 일";
    }
}
