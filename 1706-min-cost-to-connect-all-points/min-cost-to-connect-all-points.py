class Solution:
    def findMin(self, points, visited, distance):
        sol = -1
        for i in range(len(points)):
            if not visited[i] and distance[i] != -1 and (sol == -1 or distance[i] < distance[sol]):
                sol = i
        return sol
    
    def findDist(self, pointa, pointb):
        return abs(pointa[0] - pointb[0]) + abs(pointa[1] - pointb[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distance = [-1] * len(points)
        visited:List[bool] = [False] * len(points)
        distance[0] = 0
        cost = 0
        for _ in range(len(points)):
            min_index = self.findMin(points, visited, distance)
            cost += distance[min_index]
            visited[min_index] = True
            for (index, point) in enumerate(points):
                if index != min_index:
                    if (not visited[index]) and (distance[index] == -1 or distance[index] > self.findDist(point, points[min_index])):
                        distance[index] = self.findDist(point, points[min_index])
        return cost