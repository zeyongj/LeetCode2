class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        def remove_stale(pq, j):
            while pq and pq[0][1] <= j: heappop(pq)
            return -pq[0][0] if pq else 0
        ans, s, j, pq = 0, 0, -1, []
        for i in range(len(runningCosts)):
            s += runningCosts[i]
            heappush(pq, (-chargeTimes[i], i))
            while s * (i - j) + remove_stale(pq, j) > budget:
                j += 1
                s -= runningCosts[j]
            ans = max(ans, i - j)
        return ans