class Solution:
	def fabs(self,a):
		if a<0:
			return -a
		else:
			return a

	def threeSumClosest(self, num, target):
		num_items=len(num)
		if num_items==3:
			return sum(num)
		num.sort()

		absdiff=self.fabs(target)+self.fabs(num[num_items-1])+self.fabs(num[num_items-2])+self.fabs(num[num_items-3])
		output=absdiff

		for i in range(num_items-2):
			for j in range(i+1,num_items-1):
				sum2=num[i]+num[j]
				k=self.findClosest(num[j+1:num_items],target-sum2,num_items-j-1)
				if target==sum2+k:
					return sum2+k
				else:
					absd=self.fabs( target- (sum2+k) )
					if absd<=absdiff:
						absdiff=absd
						output=sum2+k
		return int(output)

	def findClosest(self,num,target,num_items):
	    #num is sorted
	    if target>=num[num_items-1]:
	    	return num[num_items-1]
	    if target<=num[0]:
	    	return num[0]
	    head=0
	    end=num_items-1
	    mid=(head+end)//2
	    while (end-head)>1:
	    	if target>=num[mid]:
	    		head=mid
	    		mid=(head+end)//2
	    	else:
	    		end=mid
	    		mid=(head+end)//2
	    if self.fabs(num[end]-target)-self.fabs(num[head]-target)>0:
	    	return num[head]
	    else:
	    	return num[end]


if __name__ == '__main__':
	s=Solution()
	n=[1,2,3,4,5,6]
	print(s.threeSumClosest([1,1,1,1], -100))
	print(s.threeSumClosest(n,0))
	print(s.threeSumClosest([-7,-71,-7,-13,45,46,-50,83,-29,-72,9,32,-74,81,68,92,-31,28,-46,-86,-70,31,-62,-20,-56,97,-41,21,81,17,-14,56,69,16,25,-38,65,-48,15,16,-25,68,-41,46,-56,-2,-3,82,8,19,-32,62,92,-56,-9,43,50,100,66,-45,41,-24,-4,83,-36,79,24,97,82,89,-56,-91,75,-64,-68,96,-55,-52,-58,-37,68,27,89,-40,-42,94,-92,-70,40,74,75,-15,54,-54,0,4,-39,93,88,-31,-26,93,8,-85,-62,89,-93,98,4,-58,8,5,-93,7,30,-75,63,41,62,-52,49,93,-11,87,7,52,5,-96,-56,43,-41,-75,-16,73,6,35,-32,62,-50,-57,-25,5,-32,94,-70,6,19,-12,63,-47,76,-57,41,-49,-33,-15,-81,55,88,67,-51,100,-19,-39,62,84,-100,78,-24,31,-32,-83,33,-25,86,9,-30,-40,52,64,-30,-17,19,-69,-89,-67,-79,-100,-53], 157))