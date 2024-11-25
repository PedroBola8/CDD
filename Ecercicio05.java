package Casa;

import java.util.Scanner;

public class Ecercicio05 {
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite F-Feminino ou M-Masculino : ");
		char resultado = entrada.next().charAt(0);
		
		if (resultado == 'F') {
			System.out.println("Feminino");
		}
		else if (resultado == 'f') {
			System.out.println("Feminino");
		}
		if (resultado == 'M') {
			System.out.println("Masculino");
		}
		else if (resultado == 'm') {
			System.out.println("Masculino");
		}
	}

}
