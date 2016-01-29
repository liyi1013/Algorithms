class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows==1 or s=='':
        	return s
        else:
        	tab=['']*numRows
        	i=0
        	flag=-1
        	for c in range(len(s)):
        		if i==0 or i==numRows-1:
        			flag=flag*(-1)
        		if flag==1:
        			tab[i]=tab[i]+s[c]
        			i+=1
        		else:
        			tab[i]=tab[i]+s[c]
        			i-=1
        	res=''
        	for i in tab:
        		res+=i
        	return res


if __name__ == '__main__':
	s=Solution()
	print s.convert('',2)
        		