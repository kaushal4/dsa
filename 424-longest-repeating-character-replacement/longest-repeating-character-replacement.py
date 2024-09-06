class Solution:
    def __init__(self) -> None:
        self.hash = dict()

    def add(self, c:str):
        if c in self.hash:
            self.hash[c] += 1
        else:
            self.hash[c] = 1


    def remove(self, c:str):
        if c in self.hash and self.hash[c] > 1:
            self.hash[c] -= 1
        else:
            self.hash.pop(c)

    # def maxChar(self) -> int:
    #     maxChar = -1
    #     for c in self.hash:
    #         maxChar = max(maxChar, self.hash[c])
    #     return maxChar

    def characterReplacement(self, s: str, k: int) -> int:
        low = -1
        high = -1
        sol = 0
        max_freq = 0

        while high < len(s) - 1:
            high = high + 1
            self.add(s[high])
            max_freq = max(max_freq, self.hash[s[high]])
            while (high - low) > (max_freq + k):
                low += 1
                self.remove(s[low])
            sol = max(sol, high - low)

        return sol