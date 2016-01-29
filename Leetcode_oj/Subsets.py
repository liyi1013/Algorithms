class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self,S):
    	output=[]
    	num_obj=len(S)
    	S.sort()
    	if num_obj==0:
    		return [output]
    	else:
    		res=self.subsets(S[0:num_obj-1])
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
    		return output

if __name__ == '__main__':
	d=[1,2,3]
	s=Solution()
	print(s.subsets([4,1,0]))

	#ss=[[],[1],[2],[1,2]]
	#temp=[]
	#print(ss)
	#for i in ss:
	#	i.append( 3 )
	#print(ss)
