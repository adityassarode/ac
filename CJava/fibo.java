
import java.util.Scanner;


class a1{
    public static void main(String[] args) {
        Scanner on = new Scanner(System.in);
        int n =nextInt();
        int a = 0;
        int b = 1;
        System.out.println(a + b);
        for (int i = 2; i < n; i++) {
            int c = a + b;
            System.out.println(c);
            a = b;
            b = c;
        }
        
    }
}




/*a=0 , b=1 = 1 , c = 1 , a =1 , b=0 , b=1,c=0
a=1,b=1,c=0

c = 2
a = 1 , b=0, b=2, c=0
a=1, b=2,c=0
c=3*/
