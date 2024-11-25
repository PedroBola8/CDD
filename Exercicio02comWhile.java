package Casa;

import java.util.Scanner;

public class Exercicio02comWhile {
	public static void main(String[] args) {
		
		int alunos = 0;
		int notas =0;
		Scanner entrada = new Scanner(System.in);
		System.out.println("Quantos alunos há na sala ? ");
		int total = entrada.nextInt();
		
		while (alunos < total) {
			System.out.println("Digite a nota do aluno: ");
			alunos = alunos +1;
			double nota = entrada.nextDouble();
			notas +=nota;
		}
		System.out.println("Notas salvas!");
		
		float media = (float) notas/total;
		System.out.println(media);
		
		
	}

}
