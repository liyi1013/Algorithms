class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        di=[]
        dj=[]
        n=len(matrix)
        if n==0 :return 
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    di.append(i)
                    dj.append(j)
        for k in di:
            for i in range(m):
                matrix[k][i]=0
        for k in dj :
            for i in range(n):
                for j in range(m):
                    if j==k:
                        matrix[i][j]=0
        print(matrix)

if __name__=='__main__':
    s=Solution()
    #m=[[1,2,3],[4,0,6],[7,8,9]]
    m=[[0]]   
    s.setZeroes(m)