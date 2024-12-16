package Encapsulamento;

/**
 * 
 */
public class Animal {
	private String nome,raça,Rg,tutor,mesversario;
	private int idade;
	
	
	public void Ajustarnome ( String nome) {
		this.nome=nome;
	}
	public void mostrarnome() {
		System.out.println(this.nome);
	}
	
	
	public void Ajustarraça (String raça) {
		this.raça=raça;
	}
	public void mostrarraça() {
		System.out.println(this.raça);
	}
	
	
	public void AjustarRg() {
		this.Rg=Rg;
	}
	public void mostrarRg() {
		System.out.println(this.Rg);
	}
	public String getTutor() {
		return tutor;
	}
	public void setTutor(String tutor) {
		this.tutor = tutor;
	}
	public String getMesversario() {
		return mesversario;
	}
	public void setMesversario(String mesversario) {
		this.mesversario = mesversario;
	}
	public int getIdade() {
		return idade;
	}
	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	
	
}
