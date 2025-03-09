class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def compare(a, b):
            if a[0] == b[0]:
                return a[1] - b[1]
            return a[0] - b[0]
        
        points.sort(key= cmp_to_key(compare))
        print(points)
        count = 0
        second_element = points[0][1]

        for point in points[1:]:
            if point[1] <= second_element:
                second_element = point[1]
            elif point[0] > second_element:
                count += 1
                second_element = point[1]
        
        count += 1
        
        return count