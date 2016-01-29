#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        n=len(nums)
        if n<3:
            return []
        res=[]
        nums=sorted(nums)

        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]: # avoid duplication
                continue
            j=i+1
            k=n-1
            while j<k:
                if j > i + 1 and nums[j] == nums[j-1]: # avoid duplication
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k+1]: # avoid duplication
                    k -= 1
                    continue
                sum_3=nums[i]+nums[j]+nums[k]
                if sum_3>0:
                    k-=1
                elif sum_3<0:
                    j+=1
                else:
                    res.append( [nums[i] , nums[j] , nums[k] ] )
                    k-=1
                    j+=1
        return res

if __name__ == '__main__':
    s=Solution()
    p=[9,-4,-5,8,-5,7,5,-6,-4,-13,9,-10,-13,-6,2,-15,-13,-9,-4,-13,-9,-9,13,-13,-9,9,-15,1,0,-14,-8,-13,-11,-5,2,0,9,14,9,-9,8,-5,-12,10,-3,5,3,-1,12,14,1,10,12,-1,13,-12,-14,13,4,-7,6,4,-5,11,6,4,-12,0,3,4,-2,-3,7,1,14,-11,-8,2,-5,11,-7,3,6,-9,9,4,-14,10,-6,-2,-11,-14,-13,-9,4,0,11,-1,-15,-9,-12,-1,3,10,7,-5,6,6,12,8,2,-9,-4,-6,-11,-9,5,-10,-14,-15,3]
    print s.threeSum(p)