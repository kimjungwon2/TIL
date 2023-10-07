import java.util.List;
import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class example1 {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1,2,3,4,5);
        Stream<Integer> intStream = list.stream(); // list를 Stream으로 변환
        intStream.forEach(System.out::print);   //forEach() 최종연산

        //stream은 1회용. Stream에 대해 최종연산을 수행하면 stream이 닫힌다.
        intStream = list.stream();  // list를 Stream으로 변환
        intStream.forEach(System.out::print);
        System.out.println();

        Stream<String> strStream = Stream.of(new String[] {"a","b","c","d"});
        strStream.forEach(System.out::println);

        int[] intArray = {1,2,3,4,5};
        IntStream intStream2 = Arrays.stream(intArray);
//        intStream2.forEach(System.out::println);

//        System.out.println(intStream2.count());
        System.out.println(intStream2.sum());

    }
}
