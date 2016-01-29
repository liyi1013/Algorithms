class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
    	len_num=len(num)
    	if(len_num==1):
    		return 0
    	if(len_num==2):
    		if(num[0]>num[1]):
    			return 0
    		else:
    			return 1
    	if(num[0]>num[1]):
    		return 0;
    	if(num[len_num-1]>num[len_num-2]):
    		return len_num-1
    	begin=0
    	end=len_num-1
    	mid=int(len_num/2)
    	while((end-begin)>1):
    		if(num[mid]<num[mid-1]):
    			end=mid
    			mid=int((begin+end)/2)
    		elif(num[mid]<num[mid+1]):
    			begin=mid
    			mid=int((begin+end)/2)+1
    		else:
    			return mid
    	return mid

s=Solution()
n=[1,2,3,4,5]
res=s.findPeakElement(n)
print("n [",res,"] =",n[res])