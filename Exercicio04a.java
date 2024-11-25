package Casa;

import java.util.Scanner;

public class Exercicio04a {
	public static void main(String[] args) {

		Scanner eu = new Scanner(System.in);
		System.out.println("Digite as notas: ");
		
		double N1 = eu.nextDouble();
		double N2 = eu.nextDouble();
		double N3 = eu.nextDouble();
		
		float media = (float) (N1+N2+N3)/3;
		System.out.println(media);
	}

}
