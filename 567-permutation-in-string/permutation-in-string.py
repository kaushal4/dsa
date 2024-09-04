class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        hash_s1:Dict[str, int] = dict()
        hash_s2:Dict[str, int] = dict()

        for c in s1:
            if c in hash_s1:
                hash_s1[c] += 1
            else:
                hash_s1[c] = 1
            
        for i in range(0, len(s1)):
            if s2[i] in hash_s2:
                hash_s2[s2[i]] += 1
            else:
                hash_s2[s2[i]] = 1

        if hash_s2 == hash_s1:
            return True

        high = len(s1) - 1
        low = 0

        while high < len(s2) - 1:
            # remove low
            if hash_s2[s2[low]] == 1:
                hash_s2.pop(s2[low])
            else:
                hash_s2[s2[low]] -= 1
            low += 1

            high = high + 1

            if s2[high] in hash_s2:
                hash_s2[s2[high]] += 1
            else:
                hash_s2[s2[high]] = 1

            if hash_s1 == hash_s2:
                return True
        
        return False