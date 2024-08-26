class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        adj = [[] for _ in range(numCourses)]
        indgree = [0] * numCourses
        visited = [False] * numCourses
        sol = []

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indgree[pre[0]]+= 1
        
        for index, val in enumerate(indgree):
            if val == 0:
                visited[index] = True
                queue.append(index)

        while queue:
            index = queue.popleft()
            sol.append(index)
            for child in adj[index]:
                if visited[child] == False:
                    indgree[child] -= 1
                    if indgree[child] == 0:
                        visited[child] = True
                        queue.append(child)

        if False in visited:
            return []

        return sol