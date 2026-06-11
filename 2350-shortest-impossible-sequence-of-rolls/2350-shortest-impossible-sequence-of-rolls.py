class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res = 1
        s = set()
        for a in rolls:
            s.add(a)
            if len(s) == k:
                res += 1
                s.clear()
        return res        