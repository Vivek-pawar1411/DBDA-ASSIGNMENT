
//Sum of series :
//	1+2+3+….+n
import java.util.Scanner;

public class sumofseries {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number");
		int n = sc.nextInt();
		int sum = 0;
		for (int i = 1; i<= n; i++) {
			sum+=i;

		}
		System.out.println("the sum of series is " + sum);

	}

}
