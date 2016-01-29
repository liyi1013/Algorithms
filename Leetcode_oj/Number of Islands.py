class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
    	num_island=0
    	self.n=len(grid)
    	if(self.n<1):
    		return num_island
    	self.m=len(grid[0])
        for i in range(self.n):
        	for j in range(self.m):
        		if grid[i][j]==1:
        			num_island+=1
        			self.sink(i,j,g)
        return num_island
    def sink(self,i,j,grid):
    	if i<0 or j<0 or i>=self.n or j>=self.m or grid[i][j]==0:
    		return 0
    	else:
    		grid[i][j]=0
    		self.sink(i-1,j,grid)
    		self.sink(i+1,j,grid)
    		self.sink(i,j-1,grid)
    		self.sink(i,j+1,grid)

if __name__ == '__main__':
	s=Solution()
	g=[[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
	res=s.numIslands([[1]])
	print res