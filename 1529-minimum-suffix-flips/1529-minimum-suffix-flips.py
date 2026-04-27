class Solution:
    def minFlips(self, target: str) -> int:
        return len(list(groupby("0" + target)))-1