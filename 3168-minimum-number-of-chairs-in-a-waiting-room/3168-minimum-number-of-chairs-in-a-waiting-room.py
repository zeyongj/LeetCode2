class Solution:
    def minimumChairs(self, s: str) -> int:
        res = 0
        max_chairs = 0
        for i in s:
            if i == 'E':
                res += 1
            else:
                max_chairs = max(res, max_chairs)
                res -= 1
        max_chairs = max(res, max_chairs)
        return max_chairs        