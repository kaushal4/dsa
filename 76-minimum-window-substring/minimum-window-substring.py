class Solution:
    def findLow(self, hash):
        sol = -1
        for key in hash:
            if hash[key] and (hash[key][0] < sol or sol == -1):
                sol = hash[key][0]
        return sol 

    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        reqs = dict()
        hash = dict()
        for c in t:
            if c in reqs:
                reqs[c] += 1
            else:
                reqs[c] = 1
                hash[c] = deque()
        low = 0
        high = 0
        sol = float('inf')
        ans = ""
        n_count = len(t)
        for i,c in enumerate(s):
            if c in reqs:
                if n_count == 0 or reqs[c] == 0:
                    hash[c].popleft()
                else: 
                    if reqs[c] > 0:
                        n_count -= 1
                        reqs[c] -= 1
                hash[c].append(i)
                high = i
                low = self.findLow(hash)
            if n_count == 0:
                if sol > high - low:
                    sol = high - low
                    ans = s[low: high+1]
        return ans


                    

