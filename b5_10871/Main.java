package b5_10871;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int n = s.nextInt();
		int x = s.nextInt();
		int[] A = new int[n]; 
		
		for(int i = 0; i < n; i++)
		{
			A[i] = s.nextInt();
			if(A[i] < x)
				System.out.printf(A[i]+" ");
		}
		
		
	}

}
