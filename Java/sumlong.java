//Write a program that accepts numbers continuously as long as the number is positive and prints the 
//sum of the given numbers.
import java.util.Scanner;
public class sumlong {

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