class Solution(object):
    def bulbSwitch0(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs=[1]*(n+1)
        #print bulbs
        for i in range(2,n+1):
            for j in range(0,len(bulbs),i):
                bulbs[j]=bulbs[j]*(-1);
            #print( bulbs)
        res=0
        for i in range(1,len(bulbs)):
            if bulbs[i]>0:
                res+=1
        return res
    def bulbSwitch(self, n):
        return n**(0.5)

if __name__ == '__main__':
    s=Solution()
    print s.bulbSwitch(9)

