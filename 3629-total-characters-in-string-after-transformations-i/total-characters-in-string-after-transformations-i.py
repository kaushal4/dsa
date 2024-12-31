class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        modulo = 10**9 + 7
        @cache
        def chars(i:int):
            if i < 25:
                return 1
            return (chars(i - 26) + chars(i - 25)) % modulo
        
        count = 0
        
        for c in s:
            buffer = ord(c) - ord('b')
            count = (count + chars(t+buffer) % modulo) % modulo
        
        return count