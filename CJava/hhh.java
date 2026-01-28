import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class hhh {
    public static void main(String[] args) {

        try {
            BufferedReader br = new BufferedReader(
                new FileReader("/workspaces/ac/CJava/filename.txt")
            );

            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }

            br.close();
        }
        catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}