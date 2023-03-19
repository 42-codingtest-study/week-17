package b5_10872;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		
		int n = s.nextInt();
		int res = 1;
		for(int i = 1; i <= n; i++) {
			res *= i;
		}
		System.out.print(res);
	}

}
