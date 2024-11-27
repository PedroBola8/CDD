package Fundamentos2;

import java.util.Scanner;

public class ExerciciocomFor06 {
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		System.out.println("Quantos alunos há na sala? ");
		int total = entrada.nextInt();
		int alunos =1;
		double notas=0,media=0;
		for (int N=alunos;N <=total;N++) {
			System.out.println("Digite a nota do aluno : ");
			alunos +=1;
			notas += entrada.nextDouble();
		}

		media =(float) (notas/total);
		System.out.println(media);
	}

}
