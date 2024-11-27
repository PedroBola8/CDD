package Fundamentos2;

public class ExerciciocomFor03 {
	public static void main(String[] args) {
		for (int N=0;N<=50;N++) {
			if (N%2!=0) {
				System.out.println(N);
			}
			if (N%2==0) {
				System.out.println(N+"-");
			}
		}
	}

}
