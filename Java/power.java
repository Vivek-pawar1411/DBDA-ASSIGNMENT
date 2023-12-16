//Write a program to find m to the power n. m=3 and n=4 so 3*3*3*3
import java.util.Scanner;
public class power {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int base=0;
		int power=0;
		int ans=1;
		System.out.println("Enter the base");
		base=sc.nextInt();
		System.out.println("Enter the power");
		power=sc.nextInt();
		for(int i=1;i<=power;i++) {
			ans*=base;
		}
		System.out.println("the ans  "+base+" is "+ans);

	}

}
