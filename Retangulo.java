package Encapsulamento;

public class Retangulo {

	private int base,altura;
	
	public void Ajustarbase ( int base) {
		this.base=base;
	}
	public void mostrarbase() {
		System.out.println(this.base);
	}
	
	
	public void Ajustaraltura (int altura) {
		this.altura=altura;
	}
	
	public void mostraraltura (int altura) {
		System.out.println(this.altura);
	}
}
