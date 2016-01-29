class Solution:
    # @return an integer
    def reverse(self, x):
        a=[]
        y=0
        sign=1
        if(x<0):
            sign=-1
            x=-x
        while(x/10!=0):
            a.append(x%10)
            x=x//10
        while(a):
            y=a[0]+y*10
            del a[0]
        return y*sign
        
if __name__=="__main__":
    s=Solution()
    print(s.reverse(1))