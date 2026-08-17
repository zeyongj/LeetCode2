class Solution:
    def minSideJumps(self, arr: List[int]) -> int:
        n = len(arr) - 1
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = dp[0][2] = 1
        
        for i in range(1, n):
            for r in range(3):
                if arr[i] == r+1 or arr[i+1] == r+1:
                    dp[i][r] = float('inf')
                else:
                    dp[i][r] = min([dp[i-1][r],
                                    dp[i-1][(r+1)%3] + 1, 
                                    dp[i-1][(r+2)%3] + 1])
        return min(dp[-1])