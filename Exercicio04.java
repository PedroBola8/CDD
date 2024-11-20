package Fundamentos;

import java.util.Scanner;

public class Exercicio04 {
		public static void main(String[] args) {
			Scanner entrada = new Scanner(System.in);
			System.out.print("Digite um N°: ");
			
			System.out.print("Digite um N°: ");
			double resultado = entrada.nextDouble();
			System.out.println();
			double resultado2 = entrada.nextDouble();
			System.out.println();
			
			float soma = resultado + resultado2;
			float media = soma/2;
			System.out.println(media);
		}
}
