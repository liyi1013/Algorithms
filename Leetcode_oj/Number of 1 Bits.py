# Number of 1 Bits
# 00000000000000000000000000001011,return 3.
# 2(00000000000000000000000000000010) return 1.

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        bstr=bin(n)[2:]
        b=int(bstr)

        res=0
        if(b<0):
            return 0
        else:
            while(b>0):
                r=b%10
                b=b/10
                if(r==1):
                    res+=1
                #print "r:",r," n:",b
        return res

    def hammingWeight_1(self, n): # better
        nn=n
        count=0
        while nn:
            count+=1
            nn=nn&(nn-1)
        return count


s=Solution()
print s.hammingWeight(i)
print s.hammingWeight_1(i)