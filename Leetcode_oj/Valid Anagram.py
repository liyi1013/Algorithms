class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        d=dict()
        for i in s:
        	if i in d:d[i]+=1
        	else:   d[i]=1
        for i in t:
        	if i in d:d[i]-=1
        	else:     return False

        for i in d :
        	if d[i]!=0:
        		return False
        return True

if __name__ == '__main__':
	a=int('0')-int('1')
	print a
	s=Solution()
	print s.isAnagram('abc','cba')