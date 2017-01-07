/* Heap Sort Program
   Name: Mohd Huzaifa Faruqui
   Roll No. : 14BCS0031
   Algorithm : http://www.cs.umd.edu/~meesh/351/mount/lectures/lect13-heapsort.pdf
*/

#include<stdio.h>

void swap(int *x, int *y)
{
	int temp;
	temp=*x;
	*x=*y;
	*y=temp;
	
}

void MaxHeapify(int A[],int n, int i)
{
	/*
		A[]	= array
		n	= size of array
		i	= position to heapify
	*/
		
	int maxPos,Max;
	
	Max=A[i];
	maxPos=i;
	
	if(2*i+1<n && A[2*i+1]>Max)    // 2*i+1 is left child
	{
		Max=A[2*i+1];
		maxPos=2*i+1;
	}
	
	
	if(2*i+2<n && A[2*i+2]>Max)  // 2*i+2 is right child
	{
		Max=A[2*i+2];
		maxPos=2*i+2;
	}

	
	if(i!=maxPos)
	{
		swap(&A[i],&A[maxPos]);
		MaxHeapify(A,n,maxPos);
	}
	
}


void BuildHeap(int A[], int n)
{
	int i;
	for(i=n/2;i>=0;i--)  //for loop starts from i=n/2 (non-leaf) beacuse leaves are already a heap
	{
		MaxHeapify(A,n,i);
	}
}

void HeapSort(int A[], int n)
{
	BuildHeap(A,n);
	while(n>=2) //requires atleast 2 elements to sorted
	{
		swap(&A[0],&A[n-1]);  //Extract largest element and put it at the end
		n--;
		MaxHeapify(A,n,0);
	}
}



int main()
{
	int A[100],n,i;
	
	printf("Enter size of array ");
	scanf("%d",&n);
	
	printf("Enter elements\n");
	
	for(i=0;i<n;i++)
		scanf("%d",&A[i]);
	
	HeapSort(A,n);
	
	printf("\nPrinting sorted array\n"); 	
	
	for(i=0;i<n;i++)
		printf("%d ",A[i]);

	return 0;
}
