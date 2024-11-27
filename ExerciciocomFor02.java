package Fundamentos2;

public class ExerciciocomFor02 {
	public static void main(String[] args) {
		for (int N=0;N<=100;N++) {
			if(N>50 && N<60) {
				continue;
			}
			System.out.println(N);
		}
	}

}
