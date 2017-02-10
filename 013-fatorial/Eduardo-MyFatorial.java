import java.util.Scanner;
public class MyFatorial {
	public static void main (String[]args){
	int entrada, fatorial = 1;
	entrada = new Scanner(System.in).nextInt();
	for (int i = entrada; i>0; i--){
		fatorial = fatorial*i;
	}
	System.out.println(fatorial);
}
}