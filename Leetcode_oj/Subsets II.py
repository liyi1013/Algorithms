class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
    	output=[]
    	num_obj=len(S)
    	S.sort()
    	if num_obj==0:
    		return [output]
    	else:
    		res=self.subsetsWithDup(S[0:num_obj-1])
    		#print(res)
    		temp=[]
    		for i in res:
    			t=[]
    			for j in i:
    				t.append(j)
    			temp.append(t)

    		for i in res:
    			i.append( S[num_obj-1] )
    		output=temp+res
    		#print(res)
    		output2=[]
    		for i in output:
    			h=0
    			for j in output2:
    				if j==i:
    					h=1
    					break
    			if h==0:
    				output2.append(i)
    		return output2

if __name__ == '__main__':
	d=[1,2,2]
	s=Solution()
	print(s.subsetsWithDup(d))
	print([1,2,3]==[1,2,3])