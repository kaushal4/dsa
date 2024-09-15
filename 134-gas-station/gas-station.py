class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(0, n)]
        cum = sum(diff)
        if cum < 0 :
            return -1
        index = n
        tank = 0
        max_tank = 0
        for i in range(n-1, -1, -1):
            tank = tank + diff[i]
            if tank >= max_tank:
                index = i
                max_tank = tank
        return index