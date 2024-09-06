class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions correspond to: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0  # Starts facing north
        posx, posy = 0, 0
        
        obstacle_set = set(map(tuple, obstacles))  # Convert obstacles list to a set for O(1) lookups
        max_dist_sq = 0
        
        for command in commands:
            if command == -2:  # Turn left 90 degrees
                direction_idx = (direction_idx - 1) % 4
            elif command == -1:  # Turn right 90 degrees
                direction_idx = (direction_idx + 1) % 4
            else:
                dx, dy = directions[direction_idx]
                for _ in range(command):
                    # Check if the next step hits an obstacle
                    if (posx + dx, posy + dy) not in obstacle_set:
                        posx += dx
                        posy += dy
                        max_dist_sq = max(max_dist_sq, posx * posx + posy * posy)
                    else:
                        break  # Stop moving if we hit an obstacle
        
        return max_dist_sq