class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        k = n
        s = 0
        p = 1
        while k>0:
            r = k%10
            s+=r
            p*=r
            k = k//10
        return p-s        