class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        L, R = [0], [inf]
        for num in nums:
            while num >= R[-1]:
                R.pop()
            if num > L[-1]:
                L.append(num)
            else:
                R.append(num)
        return L[1:] + R[1:]