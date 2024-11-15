class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        start_cord = (0,0)
        n = len(grid)
        distances:Dict[Tuple[int, int], int] = {}
        heap = []
        visited:Set[Tuple[int, int]] = set()
        distances[start_cord] = grid[start_cord[0]][start_cord[1]]
        heapq.heappush(heap, (grid[start_cord[0]][start_cord[1]], start_cord)) 
        visited.add(start_cord)
        dist = [(0,1), (1, 0), (0, -1), (-1, 0)]
        
        for _ in range(n):
            for _ in range(n):
                _, min_cord = heapq.heappop(heap)
                if min_cord == (n-1, n-1):
                    return distances[min_cord]

                for (cx, cy) in dist:
                    new_x = min_cord[0] + cx
                    new_y = min_cord[1] + cy

                    if new_x < n and new_x >= 0 and new_y < n and new_y >=0 and ((new_x, new_y) not in visited):
                        visited.add((new_x, new_y))
                        distances[(new_x, new_y)] = max(grid[new_x][new_y], distances[min_cord])
                        heapq.heappush(heap, (distances[(new_x, new_y)], (new_x, new_y)))

        return distances[(n-1, n-1)]