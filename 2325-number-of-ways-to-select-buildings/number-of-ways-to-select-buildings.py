class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        dp:List[List[List[int]]] = [[[-1] * 4 for _ in range(2)] for _ in range(n)]

        def recur(req:int, index:int, prev:str) -> int:
            if(req == 0):
                return 1
            if(index >= n):
                return 0
            if dp[index][int(prev)][req] != -1:
                return dp[index][int(prev)][req]
            next_index = index
            sol = 0
            while(next_index < n and s[next_index] == s[index]):
                next_index += 1
            sol += recur(req, next_index, prev)
            if prev != s[index]:
                sol += (next_index - index) * recur(req-1, next_index, s[index])
            dp[index][int(prev)][req] = sol
            return sol
        return (recur(3, 0, '0') + recur(3, 0, '1'))