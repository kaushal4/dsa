class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        index = n
        tank = 0
        max_tank = 0
        for i in range(n-1, -1, -1):
            tank = tank + gas[i] - cost[i]
            if tank >= max_tank:
                index = i
                max_tank = tank
        return index if tank >= 0 else -1