class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
    	num_items=len(strs)
    	if num_items<1:
    		return ""
    	prefix=strs[0]
    	for i in strs[1:num_items]:
    		if len(prefix)>len(i):
    			prefix=prefix[0:len(i)]
    		min_len=min(len(i),len(prefix))
    		for j in range(min_len):
    			if prefix[j]!=i[j]:
    				prefix=prefix[0:j]
    				break
    	return prefix

if __name__ == '__main__':
	s=Solution()
	#strs=["abd","abcd","abcf","abchrg"]
	strs=["flower","flow","flight"]
	print(s.longestCommonPrefix(strs))
