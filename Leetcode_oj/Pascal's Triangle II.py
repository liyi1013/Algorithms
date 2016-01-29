class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
    	A=[1]
    	while rowIndex!=0:
    		B=self.buildrow(A,rowIndex)
    		A=B
    		rowIndex=rowIndex-1
    	print(A)
    	return A
    def buildrow(self,A,rowIndex):
    	if (rowIndex==0):
    		return A
    	else:
    		B=[1]
    		for i in range(1,len(A)):
    			B.append(A[i]+A[i-1])
    		B.append(1)
    		return B

if __name__ == '__main__':
	s=Solution()
	s.getRow(4)