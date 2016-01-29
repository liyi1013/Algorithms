from math import fabs
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
    	num_items=len(num)
    	output=num[0:3]
    	absdiff=fabs(target+num[0]+num[1]+num[2])

    	for i in range(num_items):
    		other1=self.twoSumClosest(num[0:i]+num[i+1:num_items],target-num[i])
    		print(other1)
    		other=other1[0]+other1[1]
    		if fabs( target- num[i]-other )<=absdiff:
    			absdiff=fabs( target- num[i]-other )
    			output=[num[i],other1[0],other1[1]]
    	print(output)
    	return output[0]+output[1]+output[2]

    def twoSumClosest(self,num,target):
    	num_items=len(num)
    	output=num
    	absdiff=fabs(target+num[0]+num[1])

    	for i in range(num_items):
    		other=self.oneSumClosest(num[0:i]+num[i+1:num_items],target-num[i])
    		if fabs( target- num[i]-other )<=absdiff:
    				absdiff=fabs( target- num[i]-other )
    				output=[num[i],other]
    	
    	return output

    def oneSumClosest(self,num,target):
    	num.sort()
    	num_items=len(num)
    	if target>=num[num_items-1]:
    		return num[num_items-1]
    	if target<=num[0]:
    		return num[0]
    	else:
    		output=num[0]
    		absdiff= fabs( target- num[0])
    		for i in num:
    			if fabs( target- i )<=absdiff:
    				absdiff=fabs( target- i )
    				output=i
    	return output

    def fabs(self,a):
    	if a<0:
    		return -a
    	else:
    		return a

if __name__ == '__main__':
	s=Solution()

	#print(s.twoSumClosest([-1,0,1,2,3,4,5,6],5.4))
	print(s.threeSumClosest([87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,10,20,-4,13,-17,0,11,-44,65,74,-48,30,-91,13,-53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,30,-13,-60,39,95,64,-12,45,-52,45,-44,73,97,100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,61,30,17,98,29,52,75,-73,-73,-23,-75,91,3,-57,91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,-61,-82,73,1,-10,-40,11,54,-81,20,40,-29,96,89,57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,12,17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4], -275))