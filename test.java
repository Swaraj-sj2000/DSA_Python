import java.util.Scanner;
public class test{
    public static void main(String[] args) {
	 Scanner input = new Scanner(System.in);
         double mark_avg;
         int result;
         int i;
         int s;
      //define size of array
       s = input.nextInt();
     //The array is defined "arr" and inserted marks into it.
      int[] arr = new int[s];   
      for(i=0;i<arr.length;i++)
	  {
	arr[i]=input.nextInt();
        }
mark_avg=0;
    result=arr[0];
    for(i=0;i<arr.length;i++)
    {if(arr[i]>=result)
        {result=arr[i];}
    mark_avg+=arr[i];}
    
    System.out.println(result);
    System.out.print(mark_avg/arr.length);

    }}