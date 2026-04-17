class Solution(object):
    def longestPalindrome(self, word1, word2):
        word = word1 + word2
        n = len(word)
        ans = 0
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif word[i] == word[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if i < len(word1) and j >= len(word1):  # Check if this palindrome begins with word1[i] and ends with word2[j]
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return ans