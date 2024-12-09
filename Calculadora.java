package Metodos;

public class Calculadora {
		public void somar(double a,double b) {
			double resp = a + b;
			System.out.println(resp);
		}

		public void somar(double a, double b, double c) {
			double resp = a+b+c;
			System.out.println(resp);
		}
		
		
		
		public void dimi(double a, double b) {
			double resp1 = a-b;
			System.out.println(resp1);
		}
		public void dimi (double a, double b, double c) {
			double resp1 = a-b-c;
			System.out.println(resp1);
		}
		
		
		
		public void mult (double a, double b) {
			double resp2 = a* b;
			System.out.println(resp2);
		}
		public void mult (double a, double b, double c) {
			double resp2 = a*b*c;
			System.out.println(resp2);
		}
		
		
		public void divi (double a , double b) {
			double resp3 = a/b;
			System.out.println(resp3);
		}
		public void divi (double a, double b,double c) {
			double resp3 = a/b/c;
			System.out.println(resp3);
		}
}
