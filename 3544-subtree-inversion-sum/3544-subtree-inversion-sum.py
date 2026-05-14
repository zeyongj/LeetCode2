class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        G = [[] for _ in range(n)]
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        memo = [[[None] * 2 for _ in range(k)] for _ in range(n)]
        def dfs(node, parent, d, isFlipped) -> int:
            d %= k
            if memo[node][d][isFlipped] is not None: return memo[node][d][isFlipped]
            # Option 1: don't flip here
            val1 = -nums[node] if isFlipped else nums[node]
            for child in G[node]:
                if child == parent: continue
                val1 += dfs(child, node, 0 if d == 0 else d + 1, isFlipped)
            # Option 2: flip here
            val2 = float('-inf')
            if d == 0:
                val2 = nums[node] if isFlipped else -nums[node]
                for child in G[node]:
                    if child == parent: continue
                    val2 += dfs(child, node, 1, not isFlipped)
            memo[node][d][isFlipped] = max(val1, val2)
            return memo[node][d][isFlipped]
        return dfs(0, -1, k, False)