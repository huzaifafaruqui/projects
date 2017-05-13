#include<iostream>
using namespace std;

template<typename T>
class Array{
public:
	Array(int);
	~Array();
	T &operator [](int);
	void Sort();
	int BinarySearch(T);
private:
	int size;
	T *data;
};

template<typename T>
Array<T>::Array(int sz)
{
	size = sz;
	data = new T[size];
}

template<typename T>
Array<T>::~Array()
{
	delete [] data;
}

template<typename T>
T &Array<T>::operator [](int idx)
{
	if(idx<0 or idx>=size)
	{
		cout<<"Array out of bound\n";
		exit(0);
	}
	return data[idx];
}

template<typename T>
int Array<T>::BinarySearch(T val)
{
	int lo, mid, hi, pos;
	lo = 0;
	hi = size - 1;
	pos = -1;
	while(lo<=hi)
	{
		mid = (hi - lo)/2 + lo;
		if(data[mid]<=val)
		{
			if(data[mid]==val)
			{
				pos = mid;
				break;
			}
			else
				lo = mid + 1;
		}
		else
		{
			hi = mid - 1;
		}
	}
	return pos;
}
