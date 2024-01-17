class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col):
            if (
                row<0 or row>(len(grid)-1) or
                col<0 or col>(len(grid[0])-1) or 
                (row,col) in visited 
            ):
                return
            if (grid[row][col]!="1"):
                return 
            visited.add((row,col))
            grid[row][col]="-1"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)
            dfs(row,col+1)
            

        count=0
        visited=set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1":
                    count+=1
                    dfs(row,col)
        return count