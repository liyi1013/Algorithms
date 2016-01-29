# Integer to Roman
class Solution:
    # @return a string
    def intToRoman(self, num):
        m=num//1000
        x=num%1000
        D=x//500
        x=x%500
        C=x//100
        x=x%100
        L=x//50
        x=x%50
        X=x//10
        x=x%10
        V=x//5
        x=x%5
        s=[m,D,C,L,X,V,x]
        str=[]
        for i in range(7):
            n=s[i]
            for j in range(n):
                if i==0:
                    str.append('M')
                if i==1:
                    str.append('D')
                if i==2:
                    str.append('C')                
                if i==3:
                    str.append('L')
                if i==4:
                    str.append('X')
                if i==5:
                    str.append('V')            
                if i==6:
                    str.append('I')                       
        return str
    
if __name__=='__main__':
    s=Solution()
    
    print(s.intToRoman(8))
    