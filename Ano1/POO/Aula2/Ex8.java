package Aula2;
import java.util.*;

public class Ex8 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		System.out.print("Cateto 1 : ");
		double c1 = sc.nextDouble();
		System.out.print("Cateto 2 : ");
		double c2 = sc.nextDouble();
		
		double aux= (c1*c1) +(c2*c2);
		double hip = Math.sqrt(aux);
		System.out.println("A hipotenusa tem o valor de " + hip);
		sc.close();

    }
}