# Triangle --- mininum path sum
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        depth=len(triangle)
        dp=[]
        if depth==0:
        	return 0
        for i in range(depth):
        	if i==0:
        		dp.append([triangle[i][i]])
        	else:
        		for j in range(i):
        			if j==0 :
        				dp.append([triangle[i][j]+dp[i-1][j]])
        			else:
        				dp[i].append(min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j])
        		dp[i].append(triangle[i][i]+dp[i-1][i-1])
        	print(dp)
        return min(dp[depth-1])


if __name__ == '__main__':
	s=Solution()

	t=[[2],[3,4],[6,5,7],[4,1,8,3]]
	print(t[0][0])
	print([]*5)
	print(s.minimumTotal([[2]]))