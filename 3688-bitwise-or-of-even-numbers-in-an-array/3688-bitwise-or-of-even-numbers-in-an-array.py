class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans = 0

        for i in nums:
            ans |= i * ((i + 1) % 2)

        return ans