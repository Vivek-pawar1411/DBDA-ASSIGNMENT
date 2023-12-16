
// Write a menu driven program to do following operations :
//a) Compute area of circle
//b) Compute area of rectangle
//c) Compute area of triangle
//d) Exit
//Display menu, ask choice to the user, depending on choice accept the parameters and perform the 
//operation. Continue this process until user selects exit option.
import java.util.Scanner;

public class Area {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("press 1 for Area of circle");
		System.out.println("press 2 for Area of trinagle ");
		System.out.println("press 3 for Area of Rectangle");
		int c;
		do {
			System.out.println("Enter the option");
			c = sc.nextInt();

			switch (c) {
			case 1:
				double cr = 0;
				System.out.println("Enter the number");
				float r = sc.nextFloat();
				cr = 3.14 * r * r;
				System.out.println("area of circle is " + cr);
				break;
			case 2:
				double t;
				System.out.println("Enter the base");
				double b = sc.nextDouble();
				System.out.println("Enter the height");
				double h = sc.nextDouble();
				t = (0.5)*(b*h);
				System.out.println("area of Triangle  is " + t);
				break;
			case 3:
				int a = 0;
				System.out.println("Enter the number");
				int l = sc.nextInt();
				System.out.println("Enter the number");
				int w = sc.nextInt();
				a = l * w;
				System.out.println("area of circle is " + a);
				break;
				default :
					System.out.println("invalid number");
			}
		} while (c < 4);
		System.out.println("-----Exit-----");

	}

}
