#coding=utf-8
'''
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.
'''
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
    	n=len(s)
    	if n<=1:
    		return s
    	res=length=0
    	index=0
    	for i in xrange(n):
    		if n-i <= res/2: break;
    		j=k=i
    		while k<n-1 and s[k+1]==s[k]:
    			k+=1
    		i=k+1
    		while k<n-1 and j>0 and s[k+1]==s[j-1]:
    			k+=1
    			j-=1
    		length=k-j+1
    		if length>res:
    			index=j
    			res=length
    			print s[index:index+res]
    	return s[index:index+res]

    def IsPalindrome(self,s):
    	n=len(s)
    	if n<=1:return True
    	if s[0]==s[n-1]:
    		return self.IsPalindrome(s[1:n-1])
    	else:
    		return False


if __name__ == '__main__':
	s=Solution()
	print s.longestPalindrome("ccc")