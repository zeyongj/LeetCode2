class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        evens = sum(map(lambda x: x % 2 == 0, chips))
        return min(len(chips) - evens, evens)