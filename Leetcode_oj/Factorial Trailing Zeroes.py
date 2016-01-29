# Factorial Trailing Zeroes
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):#1
        if(n<5):
            return 0
        res=0
        for i in range(5,n+1,5):
            temp=i
            while(temp%5==0):
                res+=1
                temp=temp/5
        return res
    def trailingZeroes_2(self, n):#2 ???
        if(n<5):
            return 0
        res=0
        while(n>0):
            n=n/5
            res+=n
        return res



if __name__ == '__main__':
    s=Solution()
    print(s.trailingZeroes_2(10))
    #for i in range(0,104,5):
    #    print i