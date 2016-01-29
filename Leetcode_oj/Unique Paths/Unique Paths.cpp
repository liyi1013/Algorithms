//   Unique Paths

#include<iostream>
#include<vector>
using namespace std;

//递归方法
int UniquePaths1(int n,int m)
{
    if(n==1||m==1)  return 1;
    else
    return UniquePaths1(n-1,m)+UniquePaths1(n,m-1);
}

//动态规划方法
int UniquePaths2(int n,int m)
{
    //dev c++ 中的“> >”之间要加空格，否则会认为是“>>” 输出操作符，报错
    vector<vector<int> > dp(n,vector<int>(m));
    for(int i=0;i<n;i++)
    {
            for(int j=0;j<m;j++)
            {
                    if(i==0||j==0)
                    {
                        dp[i][j]=1;
                    }
                    else
                    {
                        dp[i][j]=dp[i-1][j]+dp[i][j-1];
                    }
            }
    }
    return dp[n-1][m-1];
}

int main()
{
    //输入 n,m 表示有n行，m列
     int n,m;
     cin>>n>>m;
     int result1=UniquePaths1(n,m);
     int result2=UniquePaths2(n,m);
     cout<<endl<<result1<<endl;
     cout<<endl<<result2<<endl;
     return 0;
}
