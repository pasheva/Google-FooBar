import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        String word = userInput.nextLine();
        String output = "";
        char oppositeLetter;
        for(int i=0; i < word.length(); i++){
            char letter = word.charAt(i);
            if ((letter) >= 'a' && (letter)  <= 'z' ){
                oppositeLetter = (char) (122 - (((int)letter) - 97));
                output += oppositeLetter;
            }else{
                output += word.charAt(i);
            }
        }
        System.out.println(output);
    }
}
