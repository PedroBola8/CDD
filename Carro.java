package Metodos;

public class Carro {

	String modelo;
	String cor;
	double preço;
	boolean estado = false;
	

public Carro() {
	
}
public Carro(String modelo) {
	this.modelo=modelo;
}
public Carro(String modelo, String cor) {
	this.modelo=modelo;
	this.cor=cor;
}


public Carro(String modelo, String cor, double preço) {
	this.modelo=modelo;
	this.cor=cor;
	this.preço=preço;	
}	



	
	public void modelo() {
		System.out.println(modelo + " 2025 ");
	}
	public void cor() {
		System.out.printf("%s Cor: \n",cor);
	}
	public void preço(){
		System.out.println("O modelo custa " + preço + " mil");
	}
	public void ligar() {
		System.out.println(modelo + " ligando...");
		estado = true;
	}
	public void desligar() {
		if (estado == true) {
			System.out.println(modelo + " desligando...");
			estado = false;}
		else{
			System.out.println("O carro já está desligado");
			}
	}
	public void acelerar() {
		if (estado ==true) {
		System.out.println(" VRum Vrummmm");}
		else {
			System.out.println("O carro está desligado");
		}
	}
	public void freando() {
		if (estado ==true) {
		System.out.println("IhNnnIHNNNnNnnn");}
		else {
			System.out.println("O carro já está parado");
		}
	}
	public void batendo() {
		System.out.println("BUUUMMM");
	}
}

