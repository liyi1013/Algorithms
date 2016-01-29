class Solution:
    # @return a list of integers
    def grayCode(self, n):
        N=2**n
        res=[]
        for i in range(N):
            res.append(i)
        return res
    
    
if __name__=='__main__':
    print (2**2)
    s=Solution()
    r=s.grayCode(2)
    print(r)
    ss=Solution()
    print("jjjj")