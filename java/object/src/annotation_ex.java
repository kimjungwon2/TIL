class Parent{
    void parentMethod(){}
}

class Child extends Parent{
    @Override
    @Deprecated
    void parentMethod(){

    }
}

public class annotation_ex {
    public static void main(String[] args) {
        Child c = new Child();
    }
}
