import java.util.function.Function;
import java.util.function.Supplier;

public class Example4 {

    public static void main(String[] args) {
//        Function<String,Integer> f = (String s) -> Integer.parseInt(s);
        Function<String,Integer> f = Integer::parseInt; // 메서드 참조

        System.out.println(f.apply("100")+200);


//      Supplier<MyClass> s = ()->new MyClass();
//        Supplier<MyClass> s = MyClass::new;

//        Function<Integer, MyClass> s = (i) ->new MyClass(i);
        Function<Integer, MyClass> s = MyClass::new;

        MyClass mc = s.apply(100);
        System.out.println(mc.iv);

//        Function<Integer, int[]> f2 = (i) ->new int[i];
        Function<Integer, int[]> f2 = int[]::new; // 메서드 참조
        int[] arr =f2.apply(100);

        System.out.println(f2.apply(100).length);
    }
}

class MyClass{
    int iv;

    MyClass(int iv){
        this.iv = iv;
    }
}
