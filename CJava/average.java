import java.util.Scanner;



class av{
    public static void main(String[] argu) {
        Scanner ob = new Scanner(System.in);
       
        System.out.println("Enter: ");
        int a = ob.nextInt();
            System.out.println("Enter: ");
            int b = ob.nextInt();
            System.out.println("Enter: ");
        int c = ob.nextInt();
        double average = (a + b + c) / 3.0;
        System.out.println("avearge is: "+average);
        

      
        
    }
}