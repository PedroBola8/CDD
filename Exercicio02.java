package Fundamentos;

import java.util.Scanner;

public class Exercicio02 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um N°: ");
		
		System.out.print("Digite um N°: ");
		
		System.out.print("Digite um N°: ");
		double resultado = entrada.nextDouble();
		System.out.println();
		double resultado2 = entrada.nextDouble();
		System.out.println();
		double resultado3 = entrada.nextDouble();
		System.out.println();
		
		if(resultado > resultado2){
			if (resultado>resultado3) {
			System.out.println(resultado);
			}
			else {
				System.out.println(resultado3);
			}
		}
		else {
			if(resultado2 > resultado3){
				System.out.println(resultado2);
				}
			else {
				System.out.println(resultado3);
			}
		}
	}

}
