/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner s=new Scanner(System.in);
		int n=s.nextInt();
		int[][] a=new int[n][n];
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				a[i][j]=s.nextInt();
			}
		}
		for(int k=0;k<n+n-1;k++){
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
			if(k==i+j)
			System.out.print(a[i][j]);
		
			}}
			System.out.println();
		
		}
		
	}
}
