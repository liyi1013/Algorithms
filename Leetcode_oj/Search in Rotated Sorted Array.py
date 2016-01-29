
class Solution():
	def search1(self,A,target):
		n=len(A)
		if A[0]<=A[n-1] and(target<A[0] or target>A[n-1]):
			return -1
		if A[0]>=A[n-1] and(target<A[0] and target>A[n-1]):
			return -1

		mid=int(n/2);
		if A[mid] is target :
			return mid
		else:
			is_in_array1=self.search1(A[0:mid],target)
			is_in_array2=self.search1(A[mid:n],target)#be careful of the index
			if is_in_array2!=-1:
				return is_in_array2+mid
			return is_in_array1
if __name__ == '__main__':
	s=Solution()
	a=[278,280,281,286,287,290,2,3,4,8,9,14,15,16,21,24,25,31,32,34,36,37,42,45,51,52,54,55,60,63,66,68,69,71,76,81,83,84,85,86,87,94,97,99,106,107,110,113,114,115,118,120,121,125,134,136,137,138,142,143,147,150,152,159,160,161,165,166,174,176,178,186,187,189,190,191,195,196,198,204,212,216,217,220,221,222,225,227,229,232,237,239,242,245,251,263,264,274,275,276,277]
	print(a[1:2])
	print(s.search1(a,286))
