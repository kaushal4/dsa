class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def square_distance(a):
            return a[0] ** 2 + a[1] ** 2
        arrage = []
        for point in points:
            heapq.heappush(arrage,(square_distance(point), point))
        sol = []
        for _ in range(k):
            sol.append(heapq.heappop(arrage)[1])
        return sol
        