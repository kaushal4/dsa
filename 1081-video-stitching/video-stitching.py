class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [-1] * (time + 1)

        clips.sort(key = lambda x:x[0])

        def getDp(ts):
            if ts <= 0:
                return 0
            return dp[ts]
        
        for c in clips:
            start = c[0]
            end = c[1]
            dp2 = [-1] * (time + 1)
            for t in range(time + 1):
                if t <= end and t >= start and getDp(start) != -1:
                    dp2[t] = getDp(start) + 1 if getDp(t) == -1 else min(getDp(start) + 1, getDp(t))
                else:
                    dp2[t] = dp[t]
            dp = dp2
        if dp[0] == -1:
            return -1
        
        return dp[time]