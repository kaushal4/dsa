class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        conqer = 0
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff <= 0:
                conqer += 1
                continue
            if ladders > 0:
                heapq.heappush(heap, diff)
                ladders -= 1
            else:
                heapq.heappush(heap, diff)
                min_diff = heapq.heappop(heap)
                if bricks >= min_diff:
                    bricks -= min_diff
                else:
                    break
            conqer += 1
        return conqer
        