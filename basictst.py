
import java.util.scanner;
class sum
{ 
  public static void main(String args[])
  {   
    int i, n,sum=0,num;
    Scanner sc=new Scanner(System.in);
    System.out.println("enter hiw many no. u want to add:");
    n=sc.nextInt();
    System.out.println("enter"+n+"numbers:");
    for(i=0;i<n;i++)
     {  num=sc.nextInt();
        sum=sum+num;
     }
     System.out.println("sum of all"+n+"numbers is :",sum);
     }
  } 
