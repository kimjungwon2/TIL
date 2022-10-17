import java.util.HashMap;

public class example2 {
    public static void main(String[] args) {
        HashMap<String, Student> map =new HashMap<>();  //JDK 1.7부터 생성자 타입지정 생략 가능
        map.put("자바왕",new Student("자바왕",1,1,100,100,100));

        Student s = map.get("자바왕");
        System.out.println(map);
    }
}

class Student{
    String name = "";
    int ban;
    int no;
    int kor;
    int eng;
    int math;

    public Student(String name, int ban, int no, int kor, int eng, int math) {
        this.name = name;
        this.ban = ban;
        this.no = no;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }
}