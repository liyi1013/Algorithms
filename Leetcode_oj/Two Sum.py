class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict={}
        for i in range(len(num)):
        	if (target-num[i]) in dict:
        		#dict.get(target-num[i]) #error???
        		return [dict[target-num[i]]+1,i+1]
        	else:
        		dict[num[i]]=i

if __name__ == '__main__':
    nums=[-1,2,3,4,5]
    s=Solution()
    res=s.twoSum(nums,1)
    print(res)
    print nums[res[0]-1],nums[res[1]-1]

