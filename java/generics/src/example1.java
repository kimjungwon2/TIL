import java.util.ArrayList;

class Tv{}

class Audio{}

public class example1 {
    public static void main(String[] args) {
        ArrayList<Tv> list = new ArrayList<>();
        list.add(new Tv());

        Tv t = list.get(0);
    }
}
