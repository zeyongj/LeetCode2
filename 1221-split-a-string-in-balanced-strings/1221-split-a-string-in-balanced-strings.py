class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        countR = 0
        count = 0
        for x in s:
            if x == 'L':
                countL += 1
            if x == 'R':
                countR += 1
            if countL == countR:
                count += 1
                countL = 0
                countR = 0
        return count