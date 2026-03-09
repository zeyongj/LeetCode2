class Solution:
    def zigZagArrays(self, N, L, R):
        MOD = 10 ** 9 + 7

        M = R - L + 1
        dp = [[0] * M for _ in range(N)]
        dp[0] = [1] * M
        for i in range(1, N):
            if i & 1:
                s = sum(dp[i-1]) % MOD
                for v in range(M-1, -1, -1):
                    s -= dp[i-1][v]
                    s %= MOD
                    dp[i][v] = s
            else:
                s = sum(dp[i-1]) % MOD
                for v in range(M):
                    s -= dp[i-1][v]
                    s %= MOD
                    dp[i][v] = s
        
        return sum(dp[-1]) * 2 % MOD