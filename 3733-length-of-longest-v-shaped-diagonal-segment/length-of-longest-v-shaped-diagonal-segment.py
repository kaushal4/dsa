class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # check dimensions and declare directions
        n = len(grid)
        m = len(grid[0])
        directions = {0:(1,1), 1:(1,-1), 2:(-1,-1), 3:(-1,1)}
        
        # helper function is valid with number expectation
        def isValid(x:int, y:int, expectation:int):
            if x >= n or x < 0 or y >= m or y < 0 or grid[x][y] != expectation:
                return False
            return True
        
        # function with pos, direction, hasTurned -> returns the longest possible value
        @cache
        def value(x:int, y:int, direction:int, hasTurned:bool) -> int:
            sol = 0
            expectation = 0 if grid[x][y] == 2 else 2
            
            # Continue in the same direction
            if isValid(x + directions[direction][0], y + directions[direction][1], expectation):
                sol = max(sol, value(x + directions[direction][0], y + directions[direction][1], direction, hasTurned))
            
            # Try a clockwise 90-degree turn if haven't turned yet
            if not hasTurned:
                next_direction = (direction + 1) % 4
                if isValid(x + directions[next_direction][0], y + directions[next_direction][1], expectation):
                    sol = max(sol, value(x + directions[next_direction][0], y + directions[next_direction][1], next_direction, True))
            
            return sol + 1
        
        # iterate grid and call value function for all 1s
        sol = 0
        has_one = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    has_one = True
                    for di in directions:
                        if isValid(i + directions[di][0], j + directions[di][1], 2):
                            sol = max(sol, value(i + directions[di][0], j + directions[di][1], di, False))
        
        return sol + (1 if has_one else 0)