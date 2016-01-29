class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        val=[0]+nums
        print "val",val
        DP=[0]*(len(nums)+1)
        is_robbed=[0]*(len(nums)+1)
        for i in range(1,len(val)):
        	#f_rob=0
        	if is_robbed[i-1]==0:
        		f_rob=DP[i-1]+val[i]
        	else:
        		f_rob=DP[i-2]+val[i]
        	f_no_rob=DP[i-1]
        	if f_rob>f_no_rob:
        		DP[i]=f_rob
        		is_robbed[i]=1
        	else:
        		DP[i]=f_no_rob
        		is_robbed[i]=0
        	print i,val[i]
        	print "DP ",DP
        	print "rob",is_robbed
        print DP
        return DP[len(nums)]

if __name__ == '__main__':
	s=Solution()
	h=[1,2,3,4,5,6]

	print s.rob(h)

