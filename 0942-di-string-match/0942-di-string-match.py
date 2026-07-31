class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        result = []
        for c in s:
            if c == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        result.append(low)  # low == high
        return result        