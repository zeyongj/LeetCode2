class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        words.sort()

        ans, d = [], defaultdict(list)     

        for word in words:                                  # <-- 1)
            d[word[0]].append(word)

        for top in words:                                   # <-- 2)
            for lft in d[top[0]]:           
                if lft == top: continue

                for rgt in d[top[3]]:                       # <-- 3)
                    if rgt in {top, lft}: continue
                    
                    for bot in d[lft[3]]:                   # <-- 4)
                        if bot in {top,lft,rgt}: continue
                        if bot[3] != rgt[3]: continue
                        
                        ans.append([top, lft, rgt, bot])    # <-- 5)
        return ans