class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        thresholds = [10**3, 10**6, 10**9, 10**12, 10**15]
        for t in thresholds:
            if n >= t:
                count += (n - t + 1)
        return count