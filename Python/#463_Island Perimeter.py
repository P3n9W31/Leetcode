class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.row = len(grid)
        self.col = len(grid[0])
        neighbor = 0
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == 1:
                    neighbor = neighbor + 4 - self.countNeighbor(grid,i,j)
        return neighbor
        
    def countNeighbor(self, grid, i, j):
        neighbor = 0
        
        if i != 0 and grid[i-1][j] == 1:
            neighbor += 1
        if j != 0 and grid[i][j-1] == 1:
            neighbor += 1
        if j != self.col - 1 and grid[i][j+1] == 1:
            neighbor += 1
        if i != self.row - 1 and grid[i+1][j] == 1:
            neighbor += 1
        return neighbor