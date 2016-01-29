class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        dp=[]
        for i in range(len(A)):
            if i==0:
                dp.append(A[i])
            else:
                dp.append(max(A[i],A[i]+dp[i-1]))
        print(dp)
        return max(dp)

if __name__=='__main__':
    s=Solution()
    A=[-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(A))
    
    print(max([1,2,3,5,4]))