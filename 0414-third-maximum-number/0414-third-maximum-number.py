class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l1 = max(nums)
        l2 = float("-inf")
        l3 = float("-inf")

        for i in range(len(nums)):
            if nums[i] > l1:
                l2 = l1
                l1 = nums[i]
            if nums[i] > l2 and nums[i] < l1:
                l3 = l2
                l2 = nums[i]
            if nums[i] > l3 and nums[i] < l2 :
                l3 = nums[i]
            if l2 == min(nums):
                l3 = max(nums)
            if l1 == min(nums):
                l3 = max(nums)
        return l3