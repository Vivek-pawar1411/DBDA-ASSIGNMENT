//Accept a lowercase character from the user and check whether the character is a vowel or consonant. 
//(Hint: a, e, i, o, u are vowels)

import java.util.Scanner;
public class vowel {

	public static void main(String[] args) {
	 Scanner sc =new Scanner(System.in);
	 System.out.println("Enter the string");
	  String ch=sc.next();
	  System.out.println("lower case character is ="+ch);
	  if(ch.equals("a")) {
		  System.out.println("it is vowel");
	  }
	  else if(ch.equals("e")) {
		  System.out.println("it is vowel");
	  }
	  else if(ch.equals("i")) {
		  System.out.println("it is vowel");
	  }
	  else if(ch.equals("o")) {
		  System.out.println("it is vowel");
	  }
	  else if(ch.equals("u")) {
		  System.out.println("it is vowel");
	  }
	  else {
		System.out.println("it is consonant");
	  }
	 
	 

	}

}
