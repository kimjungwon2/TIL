public class Example1 {

    @FunctionalInterface // 함수형 인터페이스는 단 하나의 추상 메서드만 가져야 한다.
    interface MyFunction{
        public abstract int max(int a, int b);
    }

    public static void main(String[] args) {

        // Object obj = (a,b)-> a>b? a:b // 람다식 작성. 익명객체
        MyFunction f= (a,b)-> a>b?a:b;

        int value = f.max(3,5); // 함수형 인터페이스가 필요하다.

        System.out.println("value 값 :"+ value);
    }
}
