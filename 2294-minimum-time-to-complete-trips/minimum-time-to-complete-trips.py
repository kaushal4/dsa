class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def solve(time1:int):
            count = 0
            for t in time:
                count += (time1 // t)
            return count
        
        low = 1 
        high = min(time) * totalTrips
        sol = 0

        while low <= high:
            mid = low + (high - low)//2
            ans = solve(mid)
            if ans >= totalTrips:
                sol = mid
                high = mid - 1
            else:
                low = mid + 1
        return sol