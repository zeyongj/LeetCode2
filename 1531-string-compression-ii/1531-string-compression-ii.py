class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)  # Length of the input string
        dp = [[999] * 101 for _ in range(101)]  # Dynamic programming array for memoization

        # Initializing the dp array with a large value (999) to represent infinity
        for i in range(n + 1):
            for j in range(n + 1):
                dp[i][j] = 999

        dp[0][0] = 0  # Base case: 0 deletions for an empty string results in 0 compression length

        # Loop through each character of the string
        for i in range(1, n + 1):
            # Loop through possible deletion counts (0 to k)
            for j in range(k + 1):
                count, del_count = 0, 0  # Variables to store the count of consecutive characters and deletions

                # Loop backward from the current character to the beginning of the string
                for t in range(i, 0, -1):
                    if s[t - 1] == s[i - 1]:
                        count += 1  # Increment count if the characters are the same
                    else:
                        del_count += 1  # Increment deletion count if the characters are different

                    # Check if the remaining deletions are sufficient for the current substring
                    if j - del_count >= 0:
                        temp = 0

                        # Determine the compression factor based on the count of consecutive characters
                        if count >= 100:
                            temp = 3
                        elif count >= 10:
                            temp = 2
                        elif count >= 2:
                            temp = 1

                        # Update the dp array with the minimum compression length
                        dp[i][j] = min(dp[i][j], dp[t - 1][j - del_count] + 1 + temp)

                # Consider the case where a deletion is made at the current position
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        # Return the minimum compression length for the entire string with at most k deletions
        return dp[n][k]