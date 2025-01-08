class Solution:
    def calculateScore(self, s: str) -> int:
        def match(c:str):
            code = ord(c) - 97
            return abs(code - 25)
        hash = {i:[] for i in range(26)} 
        n = len(s)
        score = 0
        for i in range(n):
            if hash[match(s[i])]:
                val = hash[match(s[i])].pop()
                score += (i - val)
                continue
            hash[ord(s[i]) - 97].append(i)
        return score