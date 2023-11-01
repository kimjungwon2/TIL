package org.example;



class StringTest {
    private static final String aValue="abcde";


    public static void main(String[] args) {


            String a = new String();
            StringBuffer b = new StringBuffer();
            StringBuilder c = new StringBuilder();

            Long beforeTime = System.currentTimeMillis();

            for (int loop = 0; loop < 1000000; loop++) {
                a += aValue;
            }

            Long afterTime = System.currentTimeMillis();
            Long secDiffTime = (afterTime - beforeTime)/1000;

            System.out.println("String 연산 시간"+secDiffTime);


            Long beforeTime2 = System.currentTimeMillis();

            for (int loop = 0; loop < 1000000; loop++) {
                b.append(aValue);
            }

            Long afterTime2 = System.currentTimeMillis();
            Long secDiffTime2 = (afterTime2 - beforeTime2)/1000;

            System.out.println("StringBuffer 연산 시간"+secDiffTime2);



            Long beforeTime3 = System.currentTimeMillis();
            for (int loop = 0; loop < 1000000; loop++) {
                c.append(aValue);
            }
            Long afterTime3 = System.currentTimeMillis();
            Long secDiffTime3 = (afterTime3 - beforeTime3)/1000;

            System.out.println("StringBuilder 연산 시간"+secDiffTime3);

    }
}