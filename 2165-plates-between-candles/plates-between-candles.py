class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left_min = dict()
        right_max = dict()
        cur_min = -1
        cur_max = n
        num_plates = dict()
        plate_count = 0

        for i in range(n):
            if s[i] == '|':
                cur_min = i
                plate_count += 1
            num_plates[i] = plate_count
            left_min[i] = cur_min

        for i in range(n-1,-1,-1):
            if s[i] == '|':
                cur_max = i
            right_max[i] = cur_max
        
        
        sol:int = []
        for query in queries:
            low = query[0]
            high = query[1]
            plates = left_min[high] - right_max[low] + 1
            plates -= (num_plates[high] - (num_plates[low-1] if low >= 1 else 0))
            sol.append(max(plates, 0))

        return sol

        
