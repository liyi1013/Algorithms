class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        dp=[]
        for i in range(numRows):
            level=[]
            if i==0:
                level=[1]
                dp.append(level)
            else:
                for j in range(i+1):
                    if j==0 or j==i:
                        level.append(1)
                    else:
                        level.append(dp[i-1][j]+dp[i-1][j-1])
                dp.append(level)
        return dp
            
if __name__=='__main__':
    for i in range(1):
        print (i)
        
        s=Solution()
        print(s.generate(0))