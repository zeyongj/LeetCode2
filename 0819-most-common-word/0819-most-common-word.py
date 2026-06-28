class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph)
        paragraph = paragraph.split()
        # print(paragraph)
        freq = Counter(paragraph)
        max_freq = -sys.maxsize
        res = ""
        for x in freq:
            if x not in banned and freq[x] > max_freq:
                res = x
                max_freq = freq[x]
        return res