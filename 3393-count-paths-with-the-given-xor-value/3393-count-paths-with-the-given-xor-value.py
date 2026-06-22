class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:

        def xor_update(num: int, ctr: Counter)-> Counter:
            
            res = Counter()
            for key in ctr:
                res[key ^ num]+= ctr[key]
            return res


        m, n = len(grid), len(grid[0])

        prev = [Counter([0])] * n
        for col in range(n):
            prev[col] = xor_update(grid[0][col], prev[col - 1])
        
        for row in range(1, m):
            curr = [Counter([0])] * n
            curr[0] = xor_update(grid[row][0], prev[0])

            for col in range(1, n):
                ctr = prev[col] + curr[col-1]
                curr[col] = xor_update(grid[row][col], ctr)

            prev = curr
        
        return prev[-1][k] % (10 ** 9 +7)