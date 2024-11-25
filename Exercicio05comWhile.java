package Casa;

public class Exercicio05comWhile {
	public static void main(String[] args) {
		
		int N = 0;
		
		while (N<100) {
			N+=1;
			if (N%2==0) {
				System.out.print(N+",");
			}
			
			if (N%2!=0) {
				System.out.println(N+",");
			}
		}
	}

}
