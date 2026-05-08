class Solution:
    n = 10**6 + 5
    isPrime = [False] * n
    isPrime[0] = isPrime[1] = True
    
    for i in range(2, 1001):
        if not isPrime[i]:
            for j in range(i * i, 1000005, i):
                isPrime[j] = True

    def minJumps(self, nums: List[int]) -> int:
        length = len(nums)
        limit = nums[0]
        for c in nums:
            limit = max(limit, c)

        head = [-1] * (limit + 1)
        nxt = [-1] * length
        for i in range(length):
            val = nums[i]
            nxt[i] = head[val]
            head[val] = i

        dp = [-1] * length
        dp[0] = 0
        queue = deque([0])
        seen = set()

        while queue:
            dq = queue.popleft()

            if dq == length - 1:
                return dp[dq]

            right = dq + 1
            if right < length and dp[right] == -1:
                dp[right] = dp[dq] + 1
                queue.append(right)

            left = dq - 1
            if left >= 0 and dp[left] == -1:
                dp[left] = dp[dq] + 1
                queue.append(left)

            val = nums[dq]
            if not Solution.isPrime[val] and val not in seen:
                seen.add(val)
                for i in range(val, limit + 1, val):
                    j = head[i]
                    while j != -1:
                        if dp[j] == -1:
                            dp[j] = dp[dq] + 1
                            queue.append(j)
                        j = nxt[j]
                    head[i] = -1
        return -1