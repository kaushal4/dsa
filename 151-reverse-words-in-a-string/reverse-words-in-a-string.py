class Solution:
    def reverse(self, s: list, start: int, end: int) -> None:
        mid = (end - start) // 2
        for i in range(mid + 1):
            s[start + i], s[end - i] = s[end - i], s[start + i]
    
    def removeWhite(self, s:list):
        prev = False
        i = 0
        while i < len(s):
            if prev == False and s[i] == ' ':
                del s[i]
                i -= 1
            if s[i] == ' ':
                prev = False
            else:
                prev = True
            i += 1


    def reverseWords(self, s: str) -> str:
        s = list(s)
        self.removeWhite(s)
        
        self.reverse(s, 0, len(s) - 1)
        
        prev = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, prev, i - 1)
                prev = i + 1
        
        self.reverse(s, prev, len(s) - 1)
        
        return ''.join(s).strip()