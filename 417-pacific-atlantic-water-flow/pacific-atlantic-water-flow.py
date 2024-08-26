class Solution:

    def __init__(self) -> None:
        self.m:int =0
        self.n:int =0
        self.reach_cache = [[]]
        self.cal = [[]]

    class Reach:
        def __init__(self) -> None:
            self.atlantic = False
            self.pacific = False
    
    def bfs(self, heights, i:int, j:int) -> Reach:
        visited = set()
        queue:Deque[Tuple[int]] = deque()
        reach:Solution.Reach = Solution.Reach()

        def addCell(x:int, y:int, par_height:int):
            if x < 0 or y < 0:
                reach.pacific = True
                return
            if y >= self.n or x >= self.m:
                reach.atlantic = True
                return

            if (par_height != -1 and par_height < heights[x][y]):
                return

            if self.cal[x][y] == True:
                reach.pacific = self.reach_cache[x][y].pacific or reach.pacific
                reach.atlantic = self.reach_cache[x][y].atlantic or reach.atlantic
                return

            if not (x,y) in visited:
                queue.append((x,y))

        addCell(i,j, -1)
        while queue:
            (x,y) = queue.popleft()
            visited.add((x,y))
            addCell(x+1, y, heights[x][y])
            addCell(x, y+1, heights[x][y])
            addCell(x-1, y, heights[x][y])
            addCell(x, y-1, heights[x][y])
        self.reach_cache[i][j] = reach
        self.cal[i][j] = True
        return reach



    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sol = []
        self.m = len(heights)
        self.n = len(heights[0])
        self.reach_cache = [[self.Reach()] * self.n for _ in range(self.m)]
        self.cal = [[False] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                reach = self.bfs(heights,i,j)
                if reach.atlantic == True and reach.pacific == True:
                    sol.append([i,j])
        return sol