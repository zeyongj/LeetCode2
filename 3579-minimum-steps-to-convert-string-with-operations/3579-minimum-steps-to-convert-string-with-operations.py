class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        def sub(s1, s2):
            def test(s1, s2):
                res = 0
                count = Counter()
                for a, b in zip(s1, s2):
                    if a == b: continue
                    if count[(b, a)]:
                        count[(b, a)] -= 1
                    else:
                        count[(a, b)] += 1
                        res += 1
                return res
            return min(test(s1, s2), test(s1, s2[::-1]) + 1)

        n = len(s1)
        dp = [0] + [inf] * n
        for j in range(n):
            for i in range(j + 1):
                dp[j + 1] = min(dp[j + 1], dp[i] + sub(s1[i:j+1], s2[i:j+1]))
        return dp[-1]