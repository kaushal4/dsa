class Solution:
    def findMin(self, distance, visited):
        sol = -1
        for i in range(len(distance)):
            if distance[i] != -1 and visited[i] != True and (sol == -1 or distance[i] < distance[sol]):
                sol = i
        return sol

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k = k-1 # 0 index
        distance = [-1] * n
        visited = [False] * n
        adj = [[] for _ in range(n)]
        for time in times:
            adj[time[0] - 1].append((time[1]-1, time[2]))
        
        distance[k] = 0


        for _ in range(n):
            min_index = self.findMin(distance, visited)
            if min_index == -1:
                return -1
            visited[min_index] = True

            for (index, weight) in adj[min_index]:
                if distance[index] == -1 or distance[index] > (distance[min_index] + weight):
                    distance[index] = (distance[min_index] + weight)
        
        return max(distance)