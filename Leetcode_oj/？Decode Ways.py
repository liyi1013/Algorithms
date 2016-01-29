class Solution:
    # @param s, a string
    # @return an integer
    '''XXX
    def numDecodings(self, s):
        n=len(s)
        num=0
        for i in s:
            #if(int(i)>0 and int(i)<10):
            if(int(i)!=0):
                num=1
            elif(n!=1):
                num=num-1
        for i in range(n-1):
            #print(s[i:i+2])
            if( int(s[i:i+2])>=10 and int(s[i:i+2])<27 ):
                num=num+1
        return num
        '''
    def numDecodings(self, s):
        n=len(s)
        if n<=1:
            return n
        num=0
        ss1=s[0:1]
        ss2=s[0:2]
        if int(ss1)<9 and int(ss1)>0 :
            num=num+1
        if int(ss2)>9 and int(ss2)<27:
            num=num+1
        s1=s[1:]
        s2=s[2:]
        n1=self.numDecodings(s1)
        n2=self.numDecodings(s2)
        print(n1,n2)
        return num+n1+n2
        
        
if __name__=="__main__":
    
    S='123'
    
    s=Solution()
    print(s.numDecodings(S))
    