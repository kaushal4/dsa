class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed = [x for _, x in sorted(zip(position, speed))]
        position = sorted(position)
        n = len(position)
        highest = float('-inf')
        count = 0
        for i in range(n-1,-1,-1):
            time = (target - position[i])/speed[i]
            if highest < time:
                highest = time
                count += 1
        return count