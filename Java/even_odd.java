//Write a program to accept an integer and check if it is even or odd.
import java.util.Scanner;
public class even_odd {

	public static void main(String[] args) {
		Scanner no=new Scanner(System.in);
		int a;
		System.out.println("enter the number");
		a=no.nextInt();
		//System.out.println(a);
		if(a % 2== 0) {
			System.out.println("it is even number");
			
		}else {
			System.out.println("it is odd number");
		}

	}

}
