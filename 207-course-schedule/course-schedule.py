class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # declare constants and initialize data - structures (indgree + adj)
        indegree = [0] * numCourses
        n = numCourses
        adj = defaultdict(lambda: [])
        q = deque()

        # create a adj list and fill indegree
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        # fill all courses with indegree 0 into q
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        # run loop while q and for each child check if indgree == 0
        while(q):
            node = q.popleft()
            for child in adj[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        # if indgree is positive, we can't complete
        for i in range(n):
            if indegree[i] > 0:
                return False

        # else we can complete
        return True