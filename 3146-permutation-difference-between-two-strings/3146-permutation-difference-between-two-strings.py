class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        indices = [0] * 26
        for i in range(len(s)):
            indices[ord(s[i]) - ord('a')] = i
        result = 0
        for i in range(len(s)):
            result += abs(i - indices[ord(t[i]) - ord('a')])
        return result        