class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def maxSubArray(A: List[int]):
            res, m = -inf, 0
            for i in A:
                m = max(i, m + i)
                res = max(res, m)
            return res
        s1, s2 = sum(nums1), sum(nums2)
        n1 = [x - y for x, y in zip(nums1,nums2)]
        n2 = [x - y for x, y in zip(nums2,nums1)]
        return max(s1 + maxSubArray(n2), s2 + maxSubArray(n1))