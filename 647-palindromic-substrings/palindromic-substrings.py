class Solution:
    def countSubstrings(self, s: str) -> str:
        n = len(s)
        if n < 0:
            return 0
        sol = 1
        sol_values = s[0]
        count = n

        # check odd
        mem = [1] * n

        for i in range(2, n, 2):
            for j in range(i, n):
                k = j - i
                if s[j] == s[k] and mem[k+1] != -1:
                    count += 1
                    mem[k] = 2 + mem[k+1]
                    if sol < mem[k]:
                        sol = mem[k]
                        sol_values = s[k:j+1]
                else:
                    mem[k] = -1

        # check even
        mem = [0] * n 

        for i in range(1, n, 2):
            for j in range(i, n):
                k = j - i
                if s[j] == s[k] and mem[k+1] != -1:
                    count += 1
                    mem[k] = 2 + mem[k+1]
                    if sol < mem[k]:
                        sol = mem[k]
                        sol_values = s[k:j+1]
                else:
                    mem[k] = -1


        return count