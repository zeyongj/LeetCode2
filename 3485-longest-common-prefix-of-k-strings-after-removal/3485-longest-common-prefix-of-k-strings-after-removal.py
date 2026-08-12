class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)
        ans = [0] * n
        mxLen = 0
        mp = {}
        for word in words:
            mxLen = max(mxLen, len(word))
            pref = ""
            for ch in word:
                pref += ch
                mp[pref] = mp.get(pref, 0) + 1
        mxFreqStr = ["" for _ in range(mxLen + 1)]
        mxFreq = [0] * (mxLen + 1)
        secMx = [0] * (mxLen + 1)
        for s, freq in mp.items():
            l = len(s)
            if freq > mxFreq[l]:
                secMx[l] = mxFreq[l]
                mxFreq[l] = freq
                mxFreqStr[l] = s
            elif freq > secMx[l]:
                secMx[l] = freq
        for i, word in enumerate(words):
            lo, hi = 0, mxLen + 1
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if mid <= len(word) and word[:mid] == mxFreqStr[mid]:
                    freq = max(mxFreq[mid] - 1, secMx[mid])
                else:
                    freq = mxFreq[mid]
                if freq < k:
                    hi = mid
                else:
                    lo = mid
            ans[i] = lo
        return ans