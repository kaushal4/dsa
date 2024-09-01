class Solution:

    def getHours(self, piles: List[int], rate:int ):
        count:int = 0
        for pile in piles:
            count += ceil(pile/rate)
        return count

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        sol = -1
        
        while( low <= high ):
            mid = low + (high - low)//2
            hours = self.getHours(piles, mid)
            if hours > h:
                low = mid + 1
            else:
                sol = min(mid, sol) if sol != -1 else mid 
                high = mid - 1
        
        return sol 