//
//// Write a program, which accepts annual basic salary of an employee and calculates and displays the 
//Income tax as per the following rules. 
//Basic: < 1, 50,000 Tax = 0
// 1, 50,000 to 3,00,000 Tax = 20% 
// > 3,00,000 Tax = 30% 
 import java.util.Scanner;

public class Employee {

	public static void main(String[] args) {
		double total = 0;

		Scanner em = new Scanner(System.in);
		System.out.println("Enter the salary");
		Double sal = em.nextDouble();
		if (sal > 1 & sal < 50000) {
			System.out.println("net tax = " + total);
		} else if (sal > 150000 & sal < 300000) {
			total = sal * 20 / 100;
			System.out.println("net tax" + total);

		} else if (sal >= 300000) {
			total = sal * 30 / 100;
			System.out.println("net tax" + total);

		}
		else {
			System.out.println("invalid");
		}
	}

}
