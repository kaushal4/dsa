class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 0:
            return 0
        sol = 1
        sol_values = s[0]
        mem = [[-1] * n for _ in range(n)]

        for i in range(n):
            mem[i][i] = 1

        for i in range(1, n):
            for j in range(i, n):
                k = j - i
                if s[j] != s[k]:
                    mem[j][k] = -1 
                    continue
                if j-1 < k + 1:
                    mem[j][k] = 2
                elif (mem[j-1][k+1] != -1):
                    mem[j][k] = max(mem[j][k], 2 + mem[j-1][k+1])

                if mem[j][k] > sol:
                    sol = mem[j][k]
                    sol_values = s[k:j+1]
        
        return sol_values