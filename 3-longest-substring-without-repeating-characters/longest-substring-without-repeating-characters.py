class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        hash = set()
        low = 0
        high = 1
        hash.add(s[low])
        sol = 1

        while high < len(s):
            while s[high] in hash:
                hash.remove(s[low])
                low += 1
            hash.add(s[high])
            sol = max(sol, high - low + 1)
            high += 1

        return sol 