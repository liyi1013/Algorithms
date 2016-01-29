''' 2014-8-13
    https://oj.leetcode.com/problems/search-insert-position/
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        A=A+[target]
        A.sort()
        return A.index(target)
        

if __name__=='__main__':
    s=Solution()
    a=[1,3,5,6]
    t=7
    print (s.searchInsert(a,t))
        