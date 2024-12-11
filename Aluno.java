package Heranca;

public class Aluno extends Pessoa {
	double nota;
	public Aluno(String nome, String cpf, String telefone) {
		super(nome, cpf, telefone);
	}
	public void sofrer() {
		System.out.println("Fazendo Prova!");
	}
	public void teuoito() {
		System.out.println("Te vira! Olha teu email não");
	}
}
