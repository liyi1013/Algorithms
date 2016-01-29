#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        n=len(nums)
        if n==None:
            return 0
        else:
            k=n-1
            while k>=0:
                if nums[k]==val:
                    del nums[k]
                k-=1
        print nums
        return len(nums)
        
    
if __name__=='__main__':
    x=[3,2,1,3]
    #print(len(x))
    #del x[2]
    print(x)
    #print(len(x))
    
    s=Solution()
    print (s.removeElement(x, 3))
