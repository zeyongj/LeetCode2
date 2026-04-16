class Solution:
    def __init__(self):
        self.preCompute: List[int] = []

    def findRight(self, s: str, t: str, sStart: int, sEnd: int, tStart: int, tEnd: int) -> int:
        start, end = tStart, tEnd
        ansIdx = tEnd + 1

        while start <= end:
            mid = start + (end - start) // 2
            if self.preCompute[mid] >= sStart:
                ansIdx = mid
                end = mid - 1
            else:
                start = mid + 1

        return ansIdx

    def minimumScore(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        ans = n

        self.preCompute = [-1] * n
        sIdx, tIdx = m - 1, n - 1
        while sIdx >= 0 and tIdx >= 0:
            if s[sIdx] == t[tIdx]:
                self.preCompute[tIdx] = sIdx
                tIdx -= 1
            sIdx -= 1

        ans = self.findRight(s, t, 0, m - 1, 0, n - 1)

        sIdx, tIdx = 0, 0
        while sIdx < m and tIdx < n:
            if s[sIdx] == t[tIdx]:
                tIdx += 1

                left = tIdx
                right = self.findRight(s, t, sIdx + 1, m - 1, tIdx, n - 1)
                right -= 1

                ans = min(ans, right - left + 1)

            sIdx += 1

        return ans