class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res=""
        for i in range(len(nums)):
            res+=str(int(nums[i][i])^1)
        return res