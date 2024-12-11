package Heranca;

public class Professor extends Pessoa {
	double salario;
	public Professor(String nome, String cpf, String telefone) {
		super(nome, cpf, telefone);
	}
	public void diversao() {
		System.out.println("Está se divertindo");
	}
	public void certificar() {
		System.out.println("Aprovado");
	}
}
