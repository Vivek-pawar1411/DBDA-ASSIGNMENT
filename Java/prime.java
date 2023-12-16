//Check if number is a prime number or not.: 
import java.util.Scanner;
public class prime {

	public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	System.out.println("Enter the number");
	int n=sc.nextInt();
	boolean flag =false;
	for(int i=2;i<n;i++) {
		if(n%i==0) {
			flag=false;
			break;
		}
		else {
		   flag=true;
		}
	}
	if(flag==false) 
		System.out.println(" not prime");
	else 
		System.out.println("prime");
	

	}

}
