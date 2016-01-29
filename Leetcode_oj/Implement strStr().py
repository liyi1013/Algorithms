#coding=utf-8
'''
Implement strStr().
Returns the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack. 

KMP
'''
class MY_KMP():
	# p : string
	def PMT(self,p):
		p_len=len(p)
		pmt=[0]*p_len
		for i in range(1,p_len):
			if pmt[i-1]==0:
				if p[0]==p[i]:
					pmt[i]=1
				else:
					pmt[i]=0
			else:#pmt[i-1]!=0:
				if p[i]==p[pmt[i-1]]:
					pmt[i]=(pmt[i-1]+1)
				else:
					pmt[i]=0
		return pmt

	# s,p　：string
	def KMP(self,s,p):
		if len(p)>len(s):return -1
		i=j=0 #i:s[i],j:p[j]
		pmt=self.PMT(p)
		while j<len(p) and i<=len(s)-len(p):
			if s[i+j]==p[j]:
				j+=1
			else:
				if j==0:
					i=i+1
				else:
					i=i+j-pmt[j-1]
					j=0
			if i>len(s)-len(p):
				return -1
		return i
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        s=MY_KMP()
        return s.KMP(haystack,needle)

if __name__ == '__main__':
	s=Solution()
	print s.strStr("mississippi", "issip")

