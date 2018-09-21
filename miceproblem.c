#include<stdio.h>
int a[20][20];
int sum=0;
void give(int i,int j,int k)
{
	if(i<0 || i>=k || j<0 || j>=k || a[i][j]==1 )
		return;
	if(i==k-1 && j==k-1)
	{	
	sum++;
	return ;
	}
	a[i][j]=1;
	give(i+1,j,k);
	give(i-1,j,k);
	give(i,j+1,k);
	give(i,j-1,k);
	a[i][j]=0;
	
}
int main()
{
	int n;
	scanf("%d",&n);
	int i;
	int j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	give(0,0,n);
	printf("%d\n",sum);
	
	return 0;
}
