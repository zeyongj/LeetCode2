class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        s=text.split(" ")
        res=[]
        if len(s)<3:
            return []
        for i in range(len(s)-2):
            if s[i]==first:
                if s[i+1]==second:
                    res.append(s[i+2])
        return res            
        