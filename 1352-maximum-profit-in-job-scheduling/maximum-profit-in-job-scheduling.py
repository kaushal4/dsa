class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        sorted_arrays = sorted(zip(endTime, startTime, profit))
        endTime, startTime, profit = map(list, zip(*sorted_arrays))

        max_possible = {} # 1-indexed
        for i in range(n-1, -1, -1):
            index = bisect.bisect_right(endTime, startTime[i])
            if index < 0 or index >= n:
                index = -1
            elif (endTime[index] != startTime[i]):
                index = index - 1

            max_possible[i+1] = index + 1 # 1 indexed

        dp = [0] * (n+1) # 1 indexed

        for i in range(0, n):
            dp[i+1] = profit[i] + dp[max_possible[i+1]]
            dp[i+1] = max(dp[i+1], dp[i])
        
        return dp[n]