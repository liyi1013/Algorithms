class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        y=x
        for i in range(n-1):
            y=y*x
        return y
    
if __name__=='__main__':
    s=Solution()
    print(s.pow(0.1, 3))