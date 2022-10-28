abstract class Unit2{
    int x,y;
    abstract void move(int x, int y);
    void stop(){
        System.out.println("멈춥니다.");
    }
}

interface Fightable{
    void move(int x, int y);
    void attack(Fightable f);
}

class Fighter extends Unit2 implements Fightable{
    public void move(int x, int y){
        System.out.println("["+x+","+y+"]로 이동");
    }

    public void attack(Fightable f){
        System.out.println(f+"를 공격");
    }
}


public class FighterTest {
    public static void main(String[] args) {
        Fighter f = new Fighter();
        f.move(100,200);
        Fighter f2 = new Fighter();
        f.attack(new Fighter());
    }
}
