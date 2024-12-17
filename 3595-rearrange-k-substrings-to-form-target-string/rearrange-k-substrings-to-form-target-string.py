class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        freq:Dict[str, int] = {}
        n = len(t)
        i = 0
        k = n // k
        while i < n:
            chunk = t[i: i+k]
            if chunk in freq:
                freq[chunk] += 1
            else:
                freq[chunk] = 1
            i = i + k
        
        i = 0
        while i < n:
            chunk = s[i: i+k]
            if chunk in freq and freq[chunk] > 0:
                freq[chunk] -= 1
            else:
                return False
            i = i + k
        return True