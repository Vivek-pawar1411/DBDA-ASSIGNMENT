//Write a program to find factorial of a given number. ex:no5  fact=5*4*3*2*1=120
import java.util.Scanner;
public class factorial {

	public static void main(String[] args) {
	 int n;
	 long fact=1;
	 Scanner sc=new Scanner(System.in);
	 System.out.println("Enter the number");
	 n=sc.nextInt();
	 for(int i=n;i>=1;i--) {
		 fact=fact*i;
		 
	 }
System.out.println("factorial= "+fact);

	}

}
