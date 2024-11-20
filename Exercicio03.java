package Fundamentos;

import java.util.Scanner;

public class Exercicio03 {
	public static void main(String[] args) {
		int resultado;
		Scanner input = new Scanner(System.in);
		System.out.println("Digite um N°: ");
		resultado = input.nextInt();
	
		if (resultado == 1) {
			System.out.println("Domingo");
		}
		else if (resultado == 2) {
			System.out.println("Segunda");
		}
		if (resultado ==3) {
			System.out.println("Terça");
		}
		else if (resultado == 4) {
			System.out.println("Quarta");
		}
		if (resultado == 5) {
			System.out.println("Quinta");
		}
		else if (resultado ==6) {
			System.out.println("Sexta");
		}
		if (resultado == 7) {
			System.out.println("Sabádo");
		}
		else {
			System.out.println("Valor Inválido");
		}
	}
}
