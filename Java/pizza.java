//Create menu driven program for Pizza Shop.And display total amount,
import java.util.Scanner;
public class pizza {

	public static void main(String[] args) {
	 System.out.println("-----Welcome to pizza shop------");
	 System.out.println("press 1 for  veg pizza");
	 System.out.println("press 2 for cheese pizza");
	 System.out.println("press 3 for margeeta pizza");
	 System.out.println("press 4 for veg loaded pizza");
	 System.out.println("press 5 for corn pizza");
	 Scanner sc=new Scanner(System.in);
	 int n;
	do {
	 System.out.println("Enter the choice");
	  n=sc.nextInt();
	 switch(n) {
	 case 1:
		 System.out.println("veg pizza at RS199");
		 break;
	 case 2:
		 System.out.println("Cheese pizza at RS299");
		 break;
	 case 3:
		 System.out.println("Margeeta pizza at RS399");
		 break;
	 case 4:
		 System.out.println("Veg pizza at RS499");
		 break;
	 case 5:
		 System.out.println("Corn pizza at RS299");
		 break;
		default :
		 System.out.println("Invalid number");
	 }
	 }while(n<6);
	 System.out.println("--------main ends-----");
	 
	 

	}

}
