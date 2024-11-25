package Casa;

import java.util.Scanner;

public class Exercicio04 {
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite as notas: ");
		
		double N1 = entrada.nextDouble();

		double N2 = entrada.nextDouble();

		float soma = (float) (N1 + N2);
		float media = soma/2;
		System.out.println(media);
		
	}

}
