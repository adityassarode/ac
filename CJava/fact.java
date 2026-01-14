import java.util.Scanner;



class an{
    public static void main(String[] args) {
        int fact=1;
        Scanner b = new Scanner(System.in);
        System.out.println("Enter: ");
        int n = b.nextInt();
        for (int i = 1; i <= n; i++) {
            fact = fact * i;

        }
        System.out.println(fact);
        
    }
}