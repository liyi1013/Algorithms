#include<iostream>
#include<vector>
using namespace std;



//int numTrees(int n, vector<int> &dp)
//{
//	for (int i = 0; i < n; i++)
//	{
//		if (i <= 1)
//			dp[i] = 1;
//		else if (i == 2)
//			dp[i] = 2;
//		else
//		{
//			for (int k = 0; k <i; k++)
//			{
//				dp[i] += (dp[i - k - 1] * dp[k]);
//			}
//		}
//	}
//	return 0;
//}



int numTrees(int n) {
	vector<int> dp(n + 1, 0);  // v3有10个元素，每个的值都是1  
	for (int i = 0; i <= n; i++)
	{
		if (i <= 1)
			dp[i] = 1;
		else if (i == 2)
			dp[i] = 2;
		else
		{
			int m = i - 1;
			for (int k = 0; k <= m; k++)
				dp[i] += (dp[m - k] * dp[k]);
		}
	}

	return dp[n];
}

int main()
{
	//vector<int> dp;
	//dp.resize(10);
	//numTrees(8, dp);

	//for each (int var in dp)
	//{
	//	cout << var << " ";
	//}

	for (int i = 0; i < 15; i++)
	{

		cout << numTrees(i) << " ";
	}

	return 0;
}