class Solution:
    # @param {integer[]} nums
    # @return {integer} 
    def firstMissingPositive(self, nums):  #my solution #wrong answer
        sum_nums_positive=0
        max_num=0
        for x in nums:
        	if x>0:
        		sum_nums_positive+=x
        		if x>max_num:
        			max_num=x
        if self.sum(max_num)-sum_nums_positive==0:
        	return max_num+1
        elif self.sum(max_num)-sum_nums_positive>0:
        	return self.sum(max_num)-sum_nums_positive
        else:#self.sum(max_num)-sum_nums_positive<0
        	pass
    def sum(self,n):
    	if n==1:
    		return 1
    	elif n>1:
    		return (1+n)*n/2
    	else:
    		return 0
    def firstMissingPositive_1(self, nums):  # good  # nice
    	n=len(nums)
    	for i in xrange(n):
    		while nums[i]>0 and nums[i]<n+1 and nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
    			nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
    			print nums
    	miss=1
    	for x in nums:
    		if x!=miss:
    			return miss
    		miss+=1
    	return miss

if __name__ == '__main__':
	s=Solution()
	print s.firstMissingPositive([3,4,-1,1])
	print s.firstMissingPositive_1([3,2,4,2])