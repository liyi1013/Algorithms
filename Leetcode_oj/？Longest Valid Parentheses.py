#coding=utf-8
class Solution:
    def isPair(self,s1,s2):
    	if (s1=='(' and s2==')'):
    		return True
    	else :
    		return False

    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if s=="":  #s为空的情况
    		return 0

    	res=0
    	max_len=0
    	t=[]

    	len_s=len(s)

    	i=1;
    	stack=[s[0]] #用一个数组来构造栈
    	while(i<len_s):
    		stack.append(s[i]) #压入栈中
    		print stack
    		len_stack=len(stack)
    		if len_stack>1:
    			if self.isPair(stack[len_stack-2],stack[len_stack-1]): # 如果成对则出栈
    				stack.pop()
    				stack.pop()
    				max_len+=2
    			else:
    				t.append(max_len)
    				res=max(res,max_len)
    				max_len=0
    			print res, max_len
    		i+=1
    	t.append(max_len)
    	res=max(res,max_len)
    	print t
    	return res
if __name__ == '__main__':
	s=Solution()
	print s.longestValidParentheses("()(()))(())")