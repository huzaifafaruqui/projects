#include<iostream>
#include<string>

#include "Array.h"

using namespace std;

int main()
{
	Array<int> A(10);
	for(int i = 0; i < 10; i++)
	{
		A[i] = 5 + i;
	}
	cout<<A.BinarySearch(6)<<"\n";

	cout<<A.BinarySearch(11)<<"\n";
	cout<<A.BinarySearch(25)<<"\n";

	Array<float> B(10);
	for(int i = 0; i < 10; i++)
	{
		B[i] = 5.2 + i;
	}
	B[6] = 11.0;
	cout<<B.BinarySearch(6.2)<<"\n";

	cout<<B.BinarySearch(11)<<"\n";
	cout<<B.BinarySearch(25)<<"\n";
	
	Array<string> C(3);
	C[0] = "Huzaifa";
	C[1] = "test";
	C[2] = "zebra";

	cout<<C.BinarySearch("zebra");

	return 0;
}