class Solution:
    # @return a string
    def countAndSay(self, n):
        if n==1:
        	return "1"
        else:
        	output=""
        	res=self.countAndSay(n-1)
        	n=1
        	i=1
        	while i<len(res):
        		if res[i-1]==res[i]:
        			n=n+1
        		else:
        			output=output+str(n)+res[i-1]
        			n=1
        		i=i+1
        	output=output+str(n)+res[i-1]
        	#print(output)
        	return output


if __name__ == '__main__':
	s=Solution()
	print(s.countAndSay(2))
	i=0