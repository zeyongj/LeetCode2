from collections import Counter

class Encrypter:
    def __init__(self, keys: list[str], values: list[str],
                 dictionary: list[str]):
        self.mapping = dict(zip(keys, values))
        self.counts = Counter()

        for word in dictionary:
            encrypted = self.encrypt(word)
            if encrypted:
                self.counts[encrypted] += 1

    def encrypt(self, word1: str) -> str:
        parts = []

        for char in word1:
            value = self.mapping.get(char)
            if value is None:
                return ""
            parts.append(value)

        return "".join(parts)

    def decrypt(self, word2: str) -> int:
        return self.counts[word2]
        
# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)