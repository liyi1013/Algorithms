///Maximum Subarray   (Best Time to Buy and Sell Stock)
///written by liyi.

#include<iostream>
#include<vector>
using namespace std;

struct node
{
	int v;
	int low;
	int high;
	node(int a, int b, int c) :v(a), low(b), high(c){};
};

node LaddR(vector<int> &p, int l, int h, int m)
{
	node r(0, m, m);
	int sum = 0;
	int lSum = INT_MIN;
	for (int i = m; i >= l; i--)
	{
		sum += p[i];
		if (sum > lSum)
		{
			lSum = sum;
			r.low = i;
		}
	}
	sum = 0;
	int rSum = INT_MIN;
	for (int i = m+1; i <= h; i++)
	{
		sum += p[i];
		if (sum > rSum)
		{
			rSum = sum;
			r.high = i;
		}
	}
	r.v = lSum + rSum;
	return r;
}
node f(vector<int> &p, int l, int h)
{
	if (l == h)
	{
		node r = { p[l], l, h };
		return r;
	}
	else
	{
		int m = (l + h) / 2;
		node left = f(p,l,m);
		node right = f(p,m+1,h);
		node mageSum = LaddR(p, l, h, m);

		if (left.v >= right.v && left.v >= mageSum.v)
			return left;
		else if (right.v >= left.v && right.v >= mageSum.v)
			return right;
		else if (mageSum.v>=right.v && mageSum.v>=left.v)
			return mageSum;
	}
}

int maxProfit(vector<int> &prices)
{
	int l = 0;
	int h = prices.size() - 1;
	node r = f(prices, l, h);
	return r.v;
}

int main()
{
	vector<int> p = { 1,-5,1};

	int l = 0;
	int h = p.size() - 1 ;

	node r = f(p, l, h);
	cout << r.v << " " << r.low << " " << r.high << endl;

	return 0;
}