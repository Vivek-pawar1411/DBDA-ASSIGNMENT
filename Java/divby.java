//Write a program to accept a number and check if it is divisible by 5 and 7.
import java.util.Scanner;
public class divby {

	public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	int a;
	System.out.println("Enter the number ");
	a=sc.nextInt();
	if(a%5==0) {
		System.out.println("it is divisible by 5");
	}
	else if(a%7==0) {
		System.out.println("it is divisible by 7");
		
	}
	else {
		System.out.println("it is invalid number");
	}
		
	}

	}


