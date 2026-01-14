public class GuessNumber {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        java.util.Random rand = new java.util.Random();
        int target = rand.nextInt(100) + 1; // 1-100
        int attempts = 0;

        System.out.println("I'm thinking of a number between 1 and 100. Try to guess it!");

        while (true) {
            System.out.print("Enter your guess: ");
            if (!sc.hasNextInt()) {
                System.out.println("Please enter a valid integer.");
                sc.next();
                continue;
            }
            int guess = sc.nextInt();
            attempts++;

            if (guess < target) {
                System.out.println("Higher.");
            } else if (guess > target) {
                System.out.println("Lower.");
            } else {
                System.out.printf("Correct! You guessed it in %d attempts.%n", attempts);
                break;
            }
        }

        sc.close();
    }
}
