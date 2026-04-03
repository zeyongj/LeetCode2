class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s, t = Counter(s), Counter(t)
        return sum(abs(s[ch] - t[ch]) for ch in 'abcdefghijklmnopqrstuvwxyz')