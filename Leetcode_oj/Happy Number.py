class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy_0(self, n):
        if n==1:
        	return True
        res=n
        while res!=1:
        	temp=0
        	while res>10:
        		temp+=(res%10)^2
        		res=res//10
        	temp+=res^2
        	print temp
        	temp=res
        return True
    def isHappy(self, n):
        if n==1:
            return True
        res=n
        s=set()
        while res!=1:
            temp=0
            while res>=10:
                temp+=(res%10)*(res%10)
                res=res//10
                #print res
            temp+=res*res
            print temp
            if temp in s:
                return False
            else:
                s.add(temp)
            res=temp
        return True

if __name__ == '__main__':
    s=Solution()
    print(s.isHappy(7))