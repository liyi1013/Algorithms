class Solution:
    # @return a boolean
    #def isPalindrome(self, x): # without extra space.
        #if x<0:
            #return False
        #n=1
        #m=10
        #while x//m != 0:
            #m=m*10
            #n+=1
        #print(n)
        #while x//10>0:
            #y=10**(n-1)
            #if x//y==x%10 :
                #x=x%y
                #x=x//10
                #print(x)
                #n-=2
            #else:
                #return False
        #return True
#s=Solution()
#print(s.isPalindrome(10000021))
    
    def isPalindrome(self, x):
        if x<0: return False    
        else:
            reversed_Num=0
            y=x
            while(y!=0):
                temp=y%10
                reversed_Num=reversed_Num*10+temp
                y=y//10 
            return reversed_Num==x
            
s=Solution()
print(s.isPalindrome(12000021))
            