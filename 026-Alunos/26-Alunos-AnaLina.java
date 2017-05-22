import java.util.*;public class S{public static void main(String[] args) {Scanner s=new Scanner(System.in);double[]no=new double[3];
	String[]n=new String[1];n[0] = s.nextLine(); no[0] = s.nextDouble();no[1] = s.nextDouble();no[2] = (no[0] + no[1])/2;
	 if(no[2]>7){
		 System.out.printf("NOME: %s\nNOTA 1: %.1f\nNOTA 2: %.1f\nMEDIA: %.1f\n",n[0],no[0],no[1],no[2]);	
			System.out.println("STATUS: APROVADA");
		}else{
			 System.out.printf("NOME: %s\nNOTA 1: %.1f\nNOTA 2: %.1f\nMEDIA: %.1f\n",n[0],no[0],no[1],no[2]);	
			System.out.println("STATUS: REPROVADA");}}} 	

