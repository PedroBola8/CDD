package Poli;

public class Vaca extends Mamiferos {

	public Vaca(String nome) {
		super(nome);
		}
	public void comer() {
		System.out.printf("%s está comendo",nome);
	}
	public void locomover() {
		System.out.printf("%s está andando",nome);
	}

}
