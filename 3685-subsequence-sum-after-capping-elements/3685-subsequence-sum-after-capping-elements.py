class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        arr = sorted(nums)

        out = [False] * n

        bitmask = 1
        limit_mask = (1 << (k + 1))-1
        add_idx = 0
        low_idx = 0

        for i in range(n):
            x = i + 1

            while add_idx < n and arr[add_idx] <= x - 1:
                val = arr[add_idx]
                shifted = bitmask << val
                bitmask = (bitmask | shifted) & limit_mask
                add_idx+=1


            while low_idx < n and arr[low_idx] < x:
                low_idx +=1
            bigger_count = n - low_idx

            
            ok = False
            upto = k // x if x else 0
            if upto > bigger_count:
                upto = bigger_count

            t = 0
            while t <= upto:
                rem = k - t *x
                if (bitmask >> rem) & 1:
                    ok = True
                    break
                t+=1
            out[i] = ok
            
        return out