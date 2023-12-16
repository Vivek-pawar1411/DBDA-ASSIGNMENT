
//Write a program to check entered number is Armstrong number or not.
import java.util.Scanner;
public class armstrong {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number");
		int a = sc.nextInt();
		int r;
		int sum = 0;
		int n;
		int temp = a;
		while (a > 0) {
			r = a % 10;
			sum += (r * r * r);
			n = a / 10;
			// System.out.println(sum);
		}
		System.out.println(sum);
		if (temp == sum) {
			System.out.println("it is armstrong");
		} else {
			System.out.println("it is not armstrong");
		}
	}

}
