package Fundamentos;

import java.util.Scanner;

public class Exercicio01 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um N°: ");
		double resultado = entrada.nextDouble();
		System.out.println(resultado);
		if (resultado > 0)
			System.out.println("N° positivo");
		else
			System.out.println("N° negativo");
			
	}

}



