class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def comp(a,b):
            if a[0] < b[0]:
                return -1
            if b[0] < a[0]:
                return 1
            return a[1] - b[1]
        
        intervals = sorted(intervals, key = cmp_to_key(comp))
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