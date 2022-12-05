import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class Main { //o nome era Socket
    static Socket s;
    static PrintWriter pw;

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        try {
            s = new Socket("DESKTOP-0UIS4QV",8000);
            pw = new PrintWriter(s.getOutputStream());
            InputStreamReader inputReader = new InputStreamReader(s.getInputStream());
            BufferedReader reader = new BufferedReader(inputReader);


            System.out.println("Jogadas Permitidas:" +
                    "rock, " +
                    "paper, " +
                    "scissors, " +
                    "lizard, " +
                    "spock");
            System.out.println("Digite sua jogada:");
            String jogada = leitor.next();

            pw = new PrintWriter(s.getOutputStream());
            pw.write(jogada);
            pw.flush();

            String res;
            while( (res=reader.readLine()) != null){
                System.out.println("Jogada do Adversário: "+res);
            }
            System.out.println("Saiu do while");
            pw.close();
            s.close();
        } catch (UnknownHostException e) {
            System.out.println("Fail");
            e.printStackTrace();
        } catch (IOException e) {
            System.out.println("Fail2");
            e.printStackTrace();
        }

    }

}