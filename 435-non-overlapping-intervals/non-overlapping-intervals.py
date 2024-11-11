class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        n = len(intervals)
        count = 0
        prev = intervals[0][1]

        for i in range(1,n):
            a = intervals[i]
            if a[0] < prev:
                count +=1
                prev = min(prev, a[1])
            else:
                prev = a[1]
        return count