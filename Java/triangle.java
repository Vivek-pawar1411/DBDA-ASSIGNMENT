//Write a C program to input angles of a triangle and check whether triangle is valid or not.

import java.util.Scanner;
public class triangle {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int a=0;
		int b=0;
		int c=0;
		int right_angle=0;
		System.out.println("Enter the angle 1");
		a=sc.nextInt();
		System.out.println("Enter the angle 2");
		b=sc.nextInt();
		System.out.println("Enter the angle 3");
		c=sc.nextInt();
		right_angle=a+b+c;
		
		if(right_angle==180){
                System.out.println("it is triangle");
	}
		else {
			System.out.println("it is not valid triangle");
		}

}
}