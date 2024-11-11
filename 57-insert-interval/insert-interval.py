class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start_val = newInterval[0]
        end_val = newInterval[1]

        index = 0
        sol = []
        n = len(intervals)
        if n == 0:
            return [newInterval]
        smallest = start_val
        largest = end_val

        while(index < n):
            if intervals[index][0] > end_val:
                sol.append([smallest, largest])
                break
            if intervals[index][1] < start_val:  
                sol.append(intervals[index])
                index += 1
                continue
            smallest = min(smallest, intervals[index][0])
            largest = max(largest, intervals[index][1])
            index +=1
        
        if len(sol) == 0 or sol[-1][1] < start_val:
            sol.append([smallest,largest])
        
        while(index < n):
            sol.append(intervals[index])
            index += 1
        
        return sol