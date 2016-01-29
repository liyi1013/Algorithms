class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        z=i=0
        n=len(A)
        if n==0:
            return 
        while i<n-1:
            r=self.xor3(A[i], A[i+1], A[i+2])
            print('r=',r)
            z=z^r
            print('z=',z)
            i=i+3
        return (A[i]^r)|z
    def xor3(self,a,b,c):
        d=a^b
        e=b^c
        return d|e

s=Solution()
print(s.xor3(1, 1, 2))
print(s.singleNumber([1,5,3,5,1,1,5,6,6,6]))
