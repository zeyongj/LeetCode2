class Solution:
    def validPalindrome(self, s: str) -> bool:
        r=len(s)-1
        def check(l,r,moves):
            while l<r:
                if s[l]!=s[r]  :
                    if moves==0:
                        return False 
                    return check(l+1,r,moves-1) or check(l,r-1,moves-1)
                l+=1
                r-=1
            return True
        return check(0,r,1)