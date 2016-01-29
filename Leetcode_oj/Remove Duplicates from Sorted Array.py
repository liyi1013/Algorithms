'''
Given a sorted array, remove the duplicates in place 
such that each element appear only once and return the new length.
'''
class Solution(object):
    def removeDuplicates(self, nums):  # time limit out
        """
        :type nums: List[int] (sorted)
        :rtype: int
        """
        n=len(nums)
        if n<=0:
            return 0
        k=n-1
        while k>0:
            for i in range(k):
                if nums[i]==nums[k]:
                    del nums[k]
                    break
            k-=1
        return len(nums)

    def removeDuplicates1(self, nums): # accpet
        n=len(nums)
        if n<=0:
            return 0
        k=n-1
        i=0
        while i<=k-1:
            if nums[i]==nums[i+1]:
                del nums[i]
                k-=1
            else:
                i+=1
        print nums
        return len(nums)

if __name__ == '__main__':
    s=Solution()
    ll=[1,1,2]
    print s.removeDuplicates(ll)
    print ll
'''
!python: 'num[:]=' not 'num='
'''
