class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num): # 203ms
        num_num=len(num)
        if (num_num<2):
        	return num[0]
        mid=int(num_num/2)
        if(num[0]>num[num_num-1]):
        	res1=self.findMin(num[0:mid])
        	res2=self.findMin(num[mid:num_num])
        	if res1<res2:
        		res=res1
        	else:
        		res=res2
        else:
        	return num[0]
        return res
    def findMin2(self, num): # 196ms
    	if(len(num)<2):
    		return num[0]
    	for x in range(1,len(num)):
    		if(num[x-1]>num[x]):
    			return num[x]
    		if(x>=len(num)-1):
    			return num[0]

s=Solution()
n=[1]
print(s.findMin2(n))