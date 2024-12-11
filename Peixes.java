package Poli;

public class Peixes extends Animal{

	public Peixes(String nome) {
		super(nome);
	}

	public void comer() {
		System.out.printf("%s está comendo",nome);
	}
	
	public void nadando() {
		System.out.printf("%s está nadando",nome);
	}
}
