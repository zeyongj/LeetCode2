class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        if not grid or not grid[0]:
            return []

        res = []
        
        for j in range(len(grid[0])):   # 1. Iterate over each column (j)
            max_width= 0

            for i in range(len(grid)):    # 2. Iterate over each row (i) to check the elements in the current column
                current_width = len(str(grid[i][j]))
                
                max_width = max(max_width, current_width)
            
            res.append(max_width)
            
        return res