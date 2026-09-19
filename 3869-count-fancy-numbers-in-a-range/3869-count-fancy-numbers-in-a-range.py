class Solution:
    def countFancy(self, l: int, r: int) -> int:
        hs = str(r)
        n = len(hs)
        ls = str(l).zfill(n)
        def check(n):
            f1, f2 = 1, 1
            s = str(n)
            for i in range(1, len(s)):
                if s[i] <= s[i-1]: f1 = 0
                if s[i] >= s[i-1]: f2 = 0
            return f1 or f2

            
        @cache    
        def fn(i, lf, hf, sm, f1, f2, prv):
            if i >= n: return 1 if f1 or f2 or check(sm) else 0
            res = 0
            lw, hi = int(ls[i]) if lf else 0, int(hs[i]) if hf else 9
            # if i == 1: print(f1, f2, prv)
            for j in range(lw, hi+1):
                # f1: inc, f2: dec
                tf1 = (prv < j and f1) if sm else 1
                tf2 = (prv > j and f2) if sm else 1
                a = fn(i+1, lf and j==lw, hf and j==hi, sm+j, tf1, tf2, j)
                res += a
                # if i == 1: print(a, f1, f2, sm+j)
            return res
        
        res = fn(0, 1, 1, 0, 1, 1, 0)
        fn.cache_clear()
        return res