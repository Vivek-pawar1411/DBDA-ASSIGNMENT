// Write a program, which accepts two integers and an operator as a character (+ - * / ), performs the 
//corresponding operation and displays the result.
import java.util.Scanner;
public class calculator {

	public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	System.out.println("Enter the number A ");
	int a=sc.nextInt();
	System.out.println("Enter the number B ");
	int b=sc.nextInt();

	System.out.println("Enter the operation");
	char ch=sc.next().charAt(0);
	int c;
	switch(ch) {
	case '+':
		c=a+b;
		System.out.println("the sum is "+c);
		break;
	case '-':
		c=a-b;
		System.out.println("the sum is "+c);
		break;
	case '*':
		c=a*b;
		System.out.println("the sum is "+c);
		break;
	case '/':
		c=a/b;
		System.out.println("the sum is "+c);
		break;
	}

	

	}

}
