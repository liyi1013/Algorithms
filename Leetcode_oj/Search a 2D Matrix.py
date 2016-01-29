class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        if target>matrix[n-1][m-1] or target<matrix[0][0]:
            return False
        head = 0
        end = n-1
        mid = (end+head)//2
        while mid>head and mid <end:
            if target<matrix[mid][0]: end=mid
            else: head=mid
            mid= (end+head)//2
        keyline=mid
        if target>matrix[keyline][m-1]: keyline+=1
        head = 0
        end = m-1
        mid = (end+head)//2
        while mid>=head and mid <end:
            if target<=matrix[keyline][mid]: end=mid
            else: head=mid+1
            mid= (end+head)//2        
        return target==matrix[keyline][mid]
   
if __name__=='__main__':
    s=Solution()
    
    matrix = [[-10],[-7],[-5]]
    target = -10
    
    m=[[1,2,3],[4,5,6],[7,8,9]]
    #m=[[1,3]]
    print(s.searchMatrix(matrix,-10))