#coding=utf-8
class Solution:
    # @return a boolean
    def isValid0(self, s): # This is Wrong Answer
    	if s=="":
    		return True
    	pair_right=set([')',']','}'])
    	len_s=len(s)
    	if len_s%2==1:
    		return False
    	if s[0] in pair_right :
    		return False
    	i=1;
    	while(i<len_s):
    		if self.isPair(s[0],s[i]):
    			break
    		else:
    			i+=1
    	print(s[1:i])
    	print(s[i+1:len_s])
    	return self.isValid(s[1:i]) and self.isValid(s[i+1:len_s]) 

    def isPair(self,s1,s2):
    	if (s1=='(' and s2==')')or (s2=='(' and s1==')'):
    		return True
    	if (s1=='[' and s2==']')or (s2=='[' and s1==']'):
    		return True
    	if (s1=='{' and s2=='}')or (s2=='{' and s1=='}'):
    		return True
    	else :
    		return False

    # 用栈来解
    def isValid(self, s):
    	if s=="":  #s为空的情况
    		return True
    	
    	pair_right=set([')',']','}'])
    	if s[0] in pair_right : #第一个就不对的情况
    		return False

    	len_s=len(s)
    	if len_s%2==1: # s 个数为奇数的情况
    		return False
    	
    	i=1;
    	stack=[s[0]] #用一个数组来构造栈
    	while(i<len_s):
    		stack.append(s[i]) #压入栈中
    		len_stack=len(stack)
    		if len_stack>1:
                # 如果成对则出栈
    			if self.isPair(stack[len_stack-1],stack[len_stack-2]): 
    				stack.pop()
    				stack.pop()
    		i+=1
    	if len(stack)==0: return True
    	else:             return False

if __name__ == '__main__':
	s=Solution()
	print(s.isValid("))]}]{([(}[[[}[}{(){})))[{(){)}[{(})(]){[)[[{}}{["))
