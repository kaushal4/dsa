class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        sol = []
        highest = intervals[0][1]
        lowest = intervals[0][0]
        for interval in intervals[1:]:
            if highest < interval[0]:
                sol.append([lowest, highest])
                lowest = interval[0]
                highest = interval[1]
            else:
                highest = max(interval[1],highest)
        sol.append([lowest, highest])
        return sol