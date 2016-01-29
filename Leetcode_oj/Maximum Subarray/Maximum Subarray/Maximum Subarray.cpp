///Maximum Subarray 
///written by liyi.

#include<iostream>
#include<vector>
using namespace std;

struct node
{
	int value;
	int low;
	int high;
	node(int a, int b, int c) :value(a), low(b), high(c){};
};

node crossSubarray(vector<int> &p, int l, int h, int m)
{
	node r(0, m, m);
	int sum = 0;
	int leftSum = INT_MIN;
	for (int i = m; i >= l; i--)
	{
		sum += p[i];
		if (sum > leftSum)
		{
			leftSum = sum;
			r.low = i;
		}
	}
	sum = 0;
	int rightSum = INT_MIN;
	for (int i = m + 1; i <= h; i++)
	{
		sum += p[i];
		if (sum > rightSum)
		{
			rightSum = sum;
			r.high = i;
		}
	}
	r.value = leftSum + rightSum;
	return r;
}
node MaxSubarray(vector<int> &p, int low, int high)
{
	if (low == high)
	{
		node r = { p[low], low, high };
		return r;
	}
	else
	{
		int m = (low + high) / 2;
		node left = MaxSubarray(p, low, m);
		node right = MaxSubarray(p, m + 1, high);
		node mageSum = crossSubarray(p, low ,high, m);

		if (left.value >= right.value && left.value >= mageSum.value)
			return left;
		else if (right.value >= left.value && right.value >= mageSum.value)
			return right;
		else if (mageSum.value >= right.value && mageSum.value >= left.value)
			return mageSum;
	}
}


int main()
{
	vector<int> p = { -11, 3, 4, -1, 2, -1, 5, 0, 7, -4, 6, 1, -8 };

	int l = 0;
	int h = p.size() - 1;

	node r = MaxSubarray(p, l, h);
	cout << "MaxSubarray sum is : "<<r.value << endl;

	cout << "MaxSubarray is : [";
	for (int i = r.low; i < r.high; i++)
	{
		cout << p[i] <<",";
	}
	cout <<p[r.high]<<"]"<<endl;

	return 0;
}

int maxProfit(vector<int> &prices)
{
	int l = 0;
	int h = prices.size() - 1;
	node r = MaxSubarray(prices, l, h);
	return r.value;
}
