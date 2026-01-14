
import java.util.Scanner;

 class a2{
     public static void main(String[] args) {
         while (true) {

             Scanner on = new Scanner(System.in);
             System.out.println("1.f to c \n 2.c to f \n 3.exit");
             System.out.println("enter choice");
             int choice = on.nextInt();
             if (choice == 1) {

                 System.out.println("enter fharnhit: ");
                 double f = on.nextDouble();
                 double c = (f * 9 / 5) + 32;

                 System.out.println("c: " + c);
             } else if (choice == 2) {

                 System.out.println("enter celsiues: ");
                 double ce = on.nextDouble();
                 double fe = (ce - 32) * 5 / 9;

                 System.out.println("f: " + fe);
             } else if (choice == 3) {

                 return;
             } else {
                 System.out.println("invlid");
             }
         }
     }
    }
    
