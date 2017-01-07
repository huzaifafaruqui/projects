/*Program Developed By oculto*/
#include<stdio.h>																																																																																										


#define FOR(i,a,n) for(i=a;i<n;i++)


int N,top;



typedef struct p{
	
	int first;
	int second;
	
}p;

p stack[100];

void push_back(int i, int j)
{
	stack[top].first=i;
	stack[top].second=j;
	top++;
} 
void pop_back()
{
	top--;
}

								
int check(int x, int y)
{	int i;
		FOR(i,0,top)
		{
			if(x==stack[i].first||y==stack[i].second||(abs(x-stack[i].first)==abs(y-stack[i].second)))
			return 0;
		}
		
return 1;		
	
}


int fill(int col)
{
	if(col>=N)
	return 1;
	int i;
	FOR(i,0,N)
	{   
		if(check(i,col))
		{     push_back(i,col);
			if(fill(col+1))
			return 1;
			pop_back();
	
		}	
	}
	return 0;
}

int main()
{  
	printf("enter n ");
	scanf("%d",&N);
	top=0;
	int i,j,k,flag;
	fill(0);
	
	FOR(i,0,N)
{	FOR(j,0,N)
	{  flag=0;
		FOR(k,0,top)
		{
			if(stack[k].first==i&&stack[k].second==j)
			flag=1;
		}
		if(flag)
		printf("* ");
		else
		printf("0 ");
	}
printf("\n");
}
printf("%d",top);

return 0;
}
