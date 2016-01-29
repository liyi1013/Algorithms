#include<iostream>
#include<vector>
using namespace std;

inline int findMin(int a, int b)
{
	if (a >= b)
		return b;
	else
		return a;
}

int shuta(vector<vector<int>> &A)
{
	int n = A.size();
	if (n < 1)
		return  0;
	if (n == 1)
		return A[0][0];
	else
	{
		vector<vector<int>> dp(n, vector<int>(n,0));
		for (int i = n-1; i >= 0; i--)
		{
			for (int j = 0; j <= i; j++)
			{
				if (i == n - 1)
				{
					dp[i][j] = A[i][j];
				}
				else
				{
					dp[i][j] = A[i][j]+ findMin(dp[i + 1][j], dp[i + 1][j + 1]);
				}
			}
		}

		for each (vector<int> var in dp)
		{
			for each (int v in var)
			{
				cout << v << " ";
			}
			cout << endl;
		}

		return dp[0][0];
	}
}

int main()
{
	//vector<vector<int>> d = { { 2, 0, 0, 0 }, { 3, 4, 0, 0 }, { 6, 5, 7, 0 }, { 4, 1, 8, 3 } };
	vector<vector<int>> d = { { 7, 0, 0, 0, 0 }, { 3, 8, 0, 0, 0 }, { 8, 1, 0, 0, 0 }, { 2, 7, 4, 4, 0 }, { 4, 5, 2, 6, 5 } };
	cout<<shuta(d)<<endl;
	return 0;
}