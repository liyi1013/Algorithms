//   Unique Paths 2

#include<iostream>
#include<vector>
using namespace std;

//��̬�滮����
int UniquePaths2(vector<vector<int> > g)
{
	//dev c++ �еġ�> >��֮��Ҫ�ӿո񣬷������Ϊ�ǡ�>>�� ���������������

	int n = g.size();
	if (n == 0) return 0;
	int m = g[0].size();

	vector<vector<int> > dp(n, vector<int>(m));
	for (int i = 0; i<n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (i == 0)
			{
				if (j == 0)
				{
					if (g[i][j] == 0)
						dp[i][j] = 1;
					else
						dp[i][j] = 0;
				}

				else
				{
					if (g[i][j] == 0)
						dp[i][j] = dp[i][j - 1];
					else
						dp[i][j] = 0;
				}
			}
			else
			{
				if (j == 0 && i != 0)
				{
					if (g[i][j] == 0)
						dp[i][j] = dp[i - 1][j];
					else
						dp[i][j] = 0;
				}

				else
				{
					if (g[i][j] == 0)
						dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
					else
						dp[i][j] = 0;
				}
			}
		}
	}
	return dp[n - 1][m - 1];
}

int main()
{

	vector<vector<int> > g;

	g = { {0,0,0,0}, { 0,1,0,0}, { 0,0,0,0} };
	//g = { { 0 }, { 1 }, { 0 } };

	int result2 = UniquePaths2(g);

	cout << endl << result2 << endl;

	return 0;
}
