package Heranca;

public class Escola {

	public static void main(String[] args) {

		Aluno a1 = new Aluno("Talita","14725369","12345677890");
		
		a1.sofrer();
		
		Professor p1 = new Professor("Wellington","11422539", "1234567890");
		p1.diversao();
		p1.certificar();
		
		
		
		a1.teuoito();
	}

}