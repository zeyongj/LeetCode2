# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        # e.g. if wordlist = ["xy", "ab", "xz"]
        # then weights = [{x: 2, a: 1}, {b: 1, y:1, z:1}]
        weights = [Counter(word[i] for word in wordlist) for i in range(6)]

        # sort wordlist, least similar to rest of corpus first
        wordlist.sort(key=lambda word: sum(weights[i][c] for i, c in enumerate(word)))

        while wordlist:
            # get the word most similar to the rest of the corpus by popping
            # from the *end* of wordlist
            word = wordlist.pop()
            matches = master.guess(word)
            # only those words that share exactly x characters with word can be
            # the solution.
            wordlist = [
                other
                for other in wordlist
                if matches == sum(w == o for w, o in zip(word, other))
            ]