class Solution:
    def possibleStringCount(self, word: str, K: int) -> int:
        MOD = 1000000007
        freq = []
        tempCount = 1
        prod = 1

        for i in range(1, len(word)+1):
            if i < len(word) and word[i] == word[i - 1]:
                tempCount += 1
            else:
                freq.append(tempCount)
                prod = (prod * tempCount) % MOD
                tempCount = 1

        if K <= len(freq):
            return prod

        dp = [0] * (K + 1)
        dp[0] = 1  # base case

        for f in reversed(freq):
            prefix = [0] * (K + 1)
            prefix[0] = dp[0]
            for k in range(1, K + 1):
                prefix[k] = (prefix[k - 1] + dp[k]) % MOD

            for k in reversed(range(K + 1)):
                count = prefix[k - 1] if k > 0 else 0
                if k > f:
                    count = count - prefix[k - f - 1]
                if k < f:
                    count = (count + (f - k) * dp[0]) % MOD
                dp[k] = count % MOD

        return dp[K]