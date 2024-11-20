package Fundamentos;

import java.util.Scanner;

public class Exercicio05 {
	public static void main(String[] args) {
		Scanner resultado1 = new Scanner(System.in);
		System.out.println("Digite F-Feminino ou M- Masculino°: ");
		char resultado = resultado1.next().charAt(0);
		
		if (resultado == 'F') {
			System.out.println("Feminimo");
		}
		else if (resultado == 'M') {
			System.out.println("Masculino");
		}
		if (resultado =='f') {
			System.out.println("feminino");
		}
		else if (resultado == 	'm') {
			System.out.println("masculino");
		}
	}
}