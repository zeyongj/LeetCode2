class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        mpp = Counter(nums)
        for count in mpp.values():
            if count > len(nums) // k:
                return False
        return len(nums) % k == 0        