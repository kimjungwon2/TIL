abstract class Player{  //추상 클래스
    abstract void play(int pos); // 추상 메서드(
    abstract void stop();   // 추상 메서드(선언부만 있고 구현부 없는 메서드)
}

//추상 클래스는 상속을 통해서 생성 가능
class AudioPlayer extends Player{
    void play(int pos){System.out.println(pos+"위치부터 play합니다.");}
    void stop(){System.out.println("재생을 멈춥니다.");}
}


public class PlayerTest{
    public static void main(String[] args) {
//        AudioPlayer ap = new AudioPlayer();
        Player ap = new AudioPlayer();  // 다형성
        ap.play(100);
        ap.stop();
    }
}