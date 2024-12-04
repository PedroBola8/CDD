package Fundamentos3;

import java.util.StringTokenizer;
import java.util.Scanner;

public class Exercicio2 {
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite uma frase");
		resultado = entrada.next();
		
		StringTokenizer exemplo = new StringTokenizer(resultado);
		 System.out.println(exemplo.countTokens());

	}

}
