class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            j = i
            while j >= 0:
                if s[j:i+1] in wordDict and dp[j] == True:
                    dp[i+1] = True
                    break
                j -= 1
        return dp[n]