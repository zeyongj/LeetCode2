class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        res=0
        max_row=[]
        max_col=[-1]*n
        
        for i in grid:
            max_row.append(max(i))
            for j in range(n):
                max_col[j]=max(max_col[j],i[j])
        
        for i in range(n):
            for j in range(n):
                res+= min(max_row[i],max_col[j])-grid[i][j]
        
        return res