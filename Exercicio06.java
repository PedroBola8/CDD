package Fundamentos;

import java.util.Scanner;

public class Exercicio06 {
		public static void main(String[] args) {
			
			Scanner pergunta1 = new Scanner(System.in);
			System.out.println("Telefonou para vítima? Digite 0-Não ou para 1-Sim : ");
			int resultado = pergunta1.nextInt();
			
			Scanner pergunta2 = new Scanner(System.in);
			System.out.println("Esteve no local do crime? Digite 0-Não ou para 1-Sim : ");
			int resultado2 = pergunta2.nextInt();
			
			Scanner pergunta3 = new Scanner(System.in);
			System.out.println("Mora perto da vítima? Digite 0-Não ou para 1-Sim : ");
			int resultado3 = pergunta3.nextInt();
			
			Scanner pergunta4 = new Scanner(System.in);
			System.out.println("Devia para vítima? Digite 0-Não ou para 1-Sim : ");
			int resultado4 = pergunta4.nextInt();
			
			Scanner pergunta5 = new Scanner(System.in);
			System.out.println("Já trabalhou com a vítima? Digite 0-Não ou para 1-Sim : ");
			int resultado5 = pergunta5.nextInt();
			
			int soma = resultado + resultado2 + resultado3 + resultado4 + resultado5;
			
			if (soma == 5) {
				System.out.println("Culpado");
			}
			else if(soma >= 3 && soma <=4) {
				System.out.println("Cumplice");
			}
			else if(soma == 2){
				System.out.println("Suspeito");
			}
			else if(soma == 1){
				System.out.println("Inocente");
			}
		}
}
