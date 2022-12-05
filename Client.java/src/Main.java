import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Main { //o nome era Socket
    static Socket s;
    static PrintWriter pw;




    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        Random gerador =new Random();
        ArrayList<String> opcoes = new ArrayList<String>();
        opcoes.add("rock");
        opcoes.add("paper");
        opcoes.add("scissors");
        opcoes.add("lizard");
        opcoes.add("spock");

        try {
            s = new Socket("DESKTOP-0UIS4QV", 8000);
            pw = new PrintWriter(s.getOutputStream());
            InputStreamReader inputReader = new InputStreamReader(s.getInputStream());
            BufferedReader reader = new BufferedReader(inputReader);
            while(true) {
//                System.out.println("Jogadas Permitidas:" +
//                        "rock, " +
//                        "paper, " +
//                        "scissors, " +
//                        "lizard, " +
//                        "spock");
//                System.out.println("Digite sua jogada:");
//                String jogada = leitor.next();

                String jog1 = opcoes.get(gerador.nextInt(5));
                pw = new PrintWriter(s.getOutputStream());
                pw.write( jog1 );
                pw.flush();
                System.out.println("\n\nVoce Jogou: " + jog1);
                String res;
                while ((res = reader.readLine()) != null) {
                    System.out.println("Jogada do Adversário: " + res);
                    break;
                }
            }
//            pw.close();
//            s.close();
        } catch (UnknownHostException e) {
            System.out.println("Fail");
            e.printStackTrace();
        } catch (IOException e) {
            System.out.println("Fim de Jogo");
            e.printStackTrace();
        }

    }

}