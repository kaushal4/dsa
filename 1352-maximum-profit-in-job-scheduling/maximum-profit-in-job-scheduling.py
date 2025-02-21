class Solution:
    def bs(self, endtime:List[int], starttime:int):
        n = len(endtime)
        low = 0
        high = n-1
        sol = -1
        while(low <= high):
            mid = low + (high-low)//2
            if endtime[mid] <= starttime:
                sol = mid
                low = mid + 1
            else:
                high = mid - 1
        return sol
                
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # sorting step
        paired_list = zip(endTime, startTime, profit)
        sorted_pairs = sorted(paired_list)
        sorted_arr1, sorted_arr2, sorted_arr3 = zip(*sorted_pairs)
        endTime, startTime, profit = list(sorted_arr1), list(sorted_arr2), list(sorted_arr3)

        #bs
        pair_index = {}
        for i in range(n):
            pair_index[i] = self.bs(endTime, startTime[i])

        # dp
        dp = [0] * n 
        dp[0] = profit[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1], profit[i] + (dp[pair_index[i]] if pair_index[i] != -1 else 0))
        return dp[n-1]