class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        digits_len=len(digits)
        if digits_len==0:
        	return []
        if digits_len==1:
        	return self.letter(digits[digits_len-1]

    def letter(self,digit):
    	
    	if digit==2:
    		return ['a','b','c']
    	if digit==3:
    		return ['d','e','f']
    	if digit==4:
    		return ['g','h','i']
    	if digit==5:
    		return ['j','k','l']
    	if digit==6:
    		return ['m','n','o']
    	if digit==7:
    		return ['p','q','r','s']
    	if digit==8:
    		return ['t','u','v']
    	if digit==9:
    		return ['w','x','y','z']
    	if digit==0:
    		return [' ']
    	else:
    		return []

if __name__ == '__main__':
	s=Solution()
	print(s.letterCombinations('5'))