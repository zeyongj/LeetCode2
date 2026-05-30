class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        ans = []
        prefix = [0] * (N+1)
        for i in range(1, N+1):
            prefix[i] += prefix[i-1] + nums[i-1]
        for q in queries:
            idx = bisect_left(nums, q)
            increments = q * idx - prefix[idx]
            decrements = prefix[N] - prefix[idx] - q * (N - idx)
            ans.append(increments + decrements)
        return ans