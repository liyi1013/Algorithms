'''
https://leetcode.com/problems/different-ways-to-add-parentheses/

Example 2

Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Output: [-34, -14, -10, -10, 10]
'''

class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input): # only for "1+2+3+4" not "11-12"
     	res=[]
    	if input is None:
    		return res
    	n=len(input)
    	if n==1:
    		return [int(input[0])]
    	for i in xrange(1,n-1,2):
    		res_l=self.diffWaysToCompute(input[:i])
    		res_r=self.diffWaysToCompute(input[i+1:n])
    		for j in xrange(len(res_l)):
    			for k in xrange(len(res_r)):
    				res.append(self.compute(res_l[j],res_r[k],input[i]))
    				pass
    			pass
    	res.sort()
    	return res
    def diffWaysToCompute_1(self, input):
        ints,operators=self.str2int(input)
        res=self.diffWaysToCompute_2(ints,operators)
        res.sort()
        return res
    def diffWaysToCompute_2(self,ints,operators):
        res=[]
        if ints is None:
            return res
        if len(ints)==1:
            return ints
        n=len(operators)
        for i in xrange(n):
            res_l=self.diffWaysToCompute_2(ints[:i+1],operators[:i])
            res_r=self.diffWaysToCompute_2(ints[i+1:],operators[i+1:])
            for j in xrange(len(res_l)):
                for k in xrange(len(res_r)):
                    res.append(self.compute(res_l[j],res_r[k],operators[i]))
        return res
    def compute(self,a,b,s):
    	if s=='+':
    		return a+b
    	if s=='-':
    		return a-b
    	if s=='*':
    		return a*b
    def str2int(self ,str):
        ints=[]
        operators=[]
        d=0
        for i in str:
            if i !='*' and i !='+' and i !='-':
                d=10*d+int(i)
            else:
                ints.append(d)
                d=0
                operators.append(i)
        ints.append(d)
        return ints,operators

if __name__ == '__main__':
	s=Solution()
	print s.diffWaysToCompute_1("2*3-4*5")