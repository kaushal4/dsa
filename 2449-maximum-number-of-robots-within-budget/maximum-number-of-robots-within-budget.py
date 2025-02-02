class Solution:
    def get_max(self, heap:List[Tuple[int, int]], low:int):
        while heap:
            (charge, index) = heap[0]
            if index > low:
                return -charge
            else:
                heapq.heappop(heap)
        return 0

    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        heap = []
        sum_costs = 0
        low = -1
        high = -1
        n = len(chargeTimes)
        sol = 0

        while(high < n-1):
            max_charge = self.get_max(heap, low)
            new_cost = ((high - low +1) * (sum_costs + runningCosts[high+1])) + max(chargeTimes[high+1], max_charge)
            if new_cost <= budget:
                high += 1
                sol = max(sol, (high - low))
                sum_costs = sum_costs + runningCosts[high]
                heapq.heappush(heap, (-chargeTimes[high], high))
            else:
                if low == high:
                    low += 1
                    high +=1
                    sum_costs = 0
                    heap = []
                else:
                    low += 1
                    sum_costs -= runningCosts[low]
        
        return sol