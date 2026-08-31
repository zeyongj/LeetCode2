class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        l, r, s = 0, len(s) - 1, list(s)
        ans = 0
        while l < r:
            if s[l] != s[r]:
                k = r
                while k > l and s[k] != s[l]:
                    k -= 1
                if k == l:
                    ans += 1
                    s[l], s[l + 1] = s[l + 1], s[l]
                else:
                    while k < r:
                        s[k], s[k + 1] = s[k + 1], s[k]
                        k += 1
                        ans += 1
                    l, r = l + 1, r - 1
            else:
                l, r = l + 1, r - 1
        return ans        