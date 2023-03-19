package b5_10869;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		int A, B;
		Scanner s = new Scanner(System.in);
		
		A = s.nextInt();
		B = s.nextInt();
		
		System.out.printf("%d \n%d \n%d \n%d \n%d", A+B, A-B, A*B, A/B, A%B);
	}

}
