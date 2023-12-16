//Write a program to find greatest of three numbers using nested if-else.
import java.util.Scanner;

public class lagrest {

	public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	System.out.println("Enter the number a ");
	int a =sc.nextInt();
	System.out.println("Enter the number b ");
	int b =sc.nextInt();
	System.out.println("Enter the number c ");
	int c =sc.nextInt();
	if(a>b & a>c) {
		System.out.println("A is lagrest number");
	}
		else if (b>a & b>c) {
			System.out.println("B is lagrest number");
		}
		else {
			System.out.println("C is a largest number");
	}
	}

}
