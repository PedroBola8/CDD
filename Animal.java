package Poli;

public class Animal {
	
	String nome;
	
	public Animal(String nome){
		this.nome=nome;
	}

	public void comer() {
		System.out.printf("%s foi comer ",nome);
	}
	
	public void locomover() {
		System.out.printf("%s está se movendo ",nome);
	}
}
