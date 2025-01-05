class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        lossc = n//2
        dp = {i:{c:0 for c in ['F', 'W', 'E']} for i in range(-lossc - 1,n+2)}
        # 1 -> won, 2 -> loss, 3 -> draw
        def compare(c1,c2):
            if c1 == 'F' and c2 == 'E':
                return 1
            if c1 == 'W' and c2 == 'F':
                return 1
            if c1 == 'E' and c2 == 'W':
                return 1
            if c1 == c2:
                return 3
            return 2
        dp[1]['F'] = 1 if compare('F', s[0]) == 1 else 0
        dp[1]['W'] = 1 if compare('W', s[0]) == 1 else 0
        dp[1]['E'] = 1 if compare('E', s[0]) == 1 else 0
        dp[0]['F'] = 1 if compare('F', s[0]) == 3 else 0
        dp[0]['W'] = 1 if compare('W', s[0]) == 3 else 0
        dp[0]['E'] = 1 if compare('E', s[0]) == 3 else 0
        dp[-1]['F'] = 1 if compare('F', s[0]) == 2 else 0
        dp[-1]['W'] = 1 if compare('W', s[0]) == 2 else 0
        dp[-1]['E'] = 1 if compare('E', s[0]) == 2 else 0

        for index in range(1,n):
            dp2 = {i:{c:0 for c in ['F', 'W', 'E']} for i in range(-lossc - 1,n+2)}
            #print(dp)
            for score in range(-lossc,n+1):
                for c in ['F', 'W', 'E']:
                    ex = ['F', 'W', 'E']
                    ex.remove(c)
                    outcome = compare(c, s[index])
                    if outcome == 1:
                        for o in ex:
                            dp2[score][c] = (dp2[score][c] + dp[score-1][o]) % MOD
                    if outcome == 2:
                        for o in ex:
                            dp2[score][c] = (dp2[score][c] + dp[score+1][o]) % MOD
                    if outcome == 3:
                        for o in ex:
                            dp2[score][c] = (dp2[score][c] + dp[score][o]) % MOD
            dp = dp2
        #print(dp)
        sol = 0
        for i in range(1, n+1):
            for c in ['F', 'W', 'E']:
                sol = (sol + dp[i][c]) % MOD
        return sol