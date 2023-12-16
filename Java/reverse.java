//Write a  program to enter a number and print its reverse.
import java.util.Scanner;

public class reverse {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int c=0;
		int b=0;
		System.out.println("Enter the number");
		int a = sc.nextInt();
		while(a!=0) {
		b=a%10;
		c=c*10+b;
		a=a/10;
		
		}
		
		System.out.println(c);
	}

}
