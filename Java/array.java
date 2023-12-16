import java.util.Scanner;
import java.util.Arrays;
public class array {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the array");
		int[] arr=new int[5];
		for (int i=0;i<arr.length;i++) {
			arr[i]=sc.nextInt();
		}
		System.out.println("display ------");
		for (int i=0;i<arr.length;i++) {
			System.out.println(arr[i]+" ");
		}
 //Arrays.sort(arr);
		System.out.println("display  sorted array------");
		for (int i=0; i>arr.length;i++) {
			System.out.println(arr[i]+" ");
		}
	}

}
