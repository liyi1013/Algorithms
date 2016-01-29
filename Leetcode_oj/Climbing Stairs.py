# https://oj.leetcode.com/problems/climbing-stairs/
# 2014-8-13  LY
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        DP=[1]*n
        print(DP)
        step=n-1
        for i in range(n):
            if(i<=1):
                DP[i]=i+1
            else:
                DP[i]=DP[i-1]+DP[i-2]
            print(DP[i]," ",i)
        return DP[step]

if __name__=="__main__":
    s=Solution()
    
    print(s.climbStairs(1))
            
        