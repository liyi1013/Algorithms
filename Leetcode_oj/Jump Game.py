class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        A_length=len(A)
        if A_length<=1 :
        	return True
        dp=[A[0]]
        if A[0]>=A_length-1:
        	return True 
        for i in range(1,A_length):
        	if dp[i-1]>=i+A[i]:
        		dp.append(dp[i-1])
        	elif dp[i-1]>=i:
        		dp.append(A[i]+i)
        	else:
        		dp.append(0)
        	if dp[i]>=A_length-1 and i<A_length-1:
        		return True
        print(dp)
        return False
if __name__ == '__main__':
	s=Solution()
	a=[1,0]
	print(s.canJump(a))
