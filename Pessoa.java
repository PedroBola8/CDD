package JavaPoo;

public class Pessoa {
	String nome;
	String idade;
	String endereço;
	public void comer() {
		System.out.println(nome + " Foi comer ");
	}
	public void dormir() {
		System.out.printf("%s Foi dormir \n",nome);
	}
	public void endereço(){
		System.out.println("Av.Rui Barbosa");
	}
	public void apresentar(){
		System.out.println(nome);
	}
	public void apresentar2(){
		System.out.println(idade);
	}
	public void apresentar3(){
		System.out.println(endereço);
	}
}
 