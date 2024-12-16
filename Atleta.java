package Acabou;

public class Atleta implements ciclista,corredor,nadador{

	@Override
	public void nadar() {
		System.out.println(" Foi nadar");
		
	}

	@Override
	public void correr() {
		System.out.println("Foi correr");
		
	}

	@Override
	public void pedalar() {
		System.out.println("Foi pedalar");
		
	}
	
}
