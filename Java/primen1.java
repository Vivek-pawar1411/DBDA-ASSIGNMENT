import java.util.Scanner;
public class primen1 {

	public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	System.out.println("Enter the number");
	int n=sc.nextInt();
	for (int i=2;i<=n ;i++){
	boolean flag =true;
	for(int j=2;j<i/2;j++) {
		if(i%j==0) {
			flag=false;
			break;
		}
		
	}
	if(flag) {
		System.out.println(" "+i);
	}

	}

	}

}
