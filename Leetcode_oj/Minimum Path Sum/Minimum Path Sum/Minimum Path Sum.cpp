//Minimum Path Sum 
#include<iostream>
#include<vector>
using namespace std;

struct node
{
	int value;
	pair<int, int> parent;
};

int minPathSum(vector<vector<int>> &grid);

int minPathSum2(vector<vector<int>> &grid)
{
	if (grid.empty())
		return 0;
	else
	{
		int n = grid.size();
		int m = grid[0].size();

		vector<vector<node>> dp(n, vector<node>(m));

		for (int i = n - 1; i >= 0; i--)
		{
			for (int j = m - 1; j >= 0; j--)
			{
				if (i == n - 1 && j == m - 1)        //dp[n-1][m-1]
				{
					dp[i][j].value = grid[i][j];
					dp[i][j].parent = pair<int, int>(i, j);
				}
				else if (i == n - 1)                 //dp[n-1][]
				{
					dp[i][j].value = dp[i][j + 1].value + grid[i][j];
					dp[i][j].parent = pair<int, int>(i, j+1);
				}
				else if (j == m - 1)                 //dp[][m-1]
				{
					dp[i][j].value = dp[i + 1][j].value + grid[i][j];
					dp[i][j].parent = pair<int, int>(i+1, j);
				}
				else                                 //dp[i][j]
				{
					if (dp[i + 1][j].value >= dp[i][j + 1].value)  ///go right
					{
						dp[i][j].value = grid[i][j] + dp[i][j + 1].value;
						dp[i][j].parent = pair<int, int>(i, j + 1);
					}
					else                                            ///go down
					{
						dp[i][j].value = grid[i][j] + dp[i + 1][j].value;
						dp[i][j].parent = pair<int, int>(i + 1, j);
					}
				}

			}
		}

		//print dp[][]
		for each (vector<node> var in dp)
		{
			for each (node v in var)
			{
				cout << v.value << " ";
			}
			cout << endl;
		}

		//print path
		node k = dp[0][0];
		cout << "(0,0)" ;
		for (int i = 0; i < m + n - 2; i++)
		{
			cout << " -> (" << k.parent.first << "," << k.parent.second << ")";
			k = dp[k.parent.first][k.parent.second];
		}
		cout << endl;
		
		//return Minimum Path Sum 
		return dp[0][0].value;
	}
}


int main()
{
	vector<vector<int>> g = { { 0, 1, 2, 1, 8, 4 }, { 1, 5, 3, 2, 3, 5 }, { 7, 2, 6, 1, 4, 2 }, { 2, 2, 9, 7, 3, 1 }, { 2, 1, 1, 2, 6, 0 } };
	cout << minPathSum2(g)<<endl;
	return 0;
}



int minPathSum(vector<vector<int>> &grid)
{
	if (grid.empty())
		return 0;
	else
	{
		int n = grid.size();
		int m = grid[0].size();

		vector<vector<int>> dp(n, vector<int>(m));

		for (int i = n - 1; i >= 0; i--)
		{
			for (int j = m - 1; j >= 0; j--)
			{
				if (i == n - 1 && j == m - 1)
					dp[i][j] = grid[i][j];
				else if (i == n - 1)
					dp[i][j] = dp[i][j + 1] + grid[i][j];
				else if (j == m - 1)
					dp[i][j] = dp[i + 1][j] + grid[i][j];
				else
					dp[i][j] = grid[i][j] + (dp[i + 1][j] >= dp[i][j + 1] ? dp[i][j + 1] : dp[i + 1][j]);
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
