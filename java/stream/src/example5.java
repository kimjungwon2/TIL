import java.util.Optional;

public class example5 {
    public static void main(String[] args) {
        int[] arr= new int[0];
        System.out.println("arr.length="+arr.length);

//        Optional<String> opt = null; // OK. 바람직X
//        Optional<String> opt = Optional.of("ABC");
        Optional<String> opt = Optional.empty();

        String str = "";

//        str=opt.orElse(""); // Optional에 저장된 값이 null이면  ""반환
        str=opt.orElseGet(()->new String());
        System.out.println("str="+str);

    }
}
