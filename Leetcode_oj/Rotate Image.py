class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if matrix==[]:
            return []
        n=len(matrix[0])
        B=[]
        for i in range(n):
            temp=[]
            for j in range(n):
                #print(matrix[n-1-j][i])
                temp.append(matrix[n-1-j][i])
            B.append(temp)
        return B

if __name__=='__main__':
    s=Solution()
    
    A=[[1,2,3],[4,5,6],[7,8,9]]
    print(s.rotate([]))