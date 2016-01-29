'''
Rotate an array of n elements to the right by k steps.
n = 7 and k = 3, the array [1,2,3,4,5,6,7] 
is rotated to [5,6,7,1,2,3,4]. 
Could you do it in-place with O(1) extra space? 
'''

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate_0(self, nums, k): # Accepted
    	res=[]
    	l=len(nums)
        for i in range(l-k,l):
        	res.append(nums[i])
        for j in range(l-k):
        	res.append(nums[j])
        for k in range(len(nums)):
        	nums[k]=res[k]
        #nums=res

    def rotate(self, nums, k): # time out 
    	l=len(nums)
        for i in range(k):
        	temp=nums[l-1]
        	for j in range(l-1):
        		nums[l-j-1]=nums[l-j-2]
        	nums[0]=temp
        print nums

if __name__ == '__main__':
	n=[1,2]
	s=Solution()
	s.rotate_0(n,1)
	print n
