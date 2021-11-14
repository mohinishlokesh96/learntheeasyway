# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
class Solution:
    #Approach1:(Breadth First Search)
    #Time Complexity:O(n) number of Nodes
    #Space Complexity:O(n) Number of Nodes
    def numIslands1(self,grid):
        islands=0
        rows = len(grid)
        cols = len(grid[0])
        def bfs(row,col):
            visited.add((row,col))
            q= [(row,col)]
            directions = [[0,-1],[0,1],[-1,0],[1,0]]
            while q:
                length = len(q)
                for _ in range(length):
                    r,c = q.pop(0)
                    for dr,dc in directions:
                        row1 = r+dr
                        col1 = c+dc
                        if ((row1) in range(rows) and (col1) in range(cols) and grid[row1][col1]=="1" and (row1,col1) not in visited):
                            q.append((row1,col1))
                            visited.add((row1,col1))
            return
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1" and (row,col) not in visited:
                    bfs(row,col)
                    islands+=1
        return islands
    #Approach2:(Depth First Search)
    #Time Compelxity:O(n) Number of Nodes
    #Space Complexity:O(n) Number of Nodes
    def numIslands2(self,grid):
        def dfs(grid,x,y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                grid[x][y]=0 
                dfs(grid, x + 1, y)
                dfs(grid, x - 1, y)
                dfs(grid, x, y + 1)
                dfs(grid, x, y - 1)

        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    cnt+=1
        return cnt
sol = Solution()
print(sol.numIslands1([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
print(sol.numIslands2([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
