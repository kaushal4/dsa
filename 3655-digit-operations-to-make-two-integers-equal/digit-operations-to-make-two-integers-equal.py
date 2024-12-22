class Solution:
    def getPrimes(self, n:int = 10000) -> List[bool]:
        if n < 2:
            return [False, False]
        
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if primes[i]:
                primes[i*i:n:i] = [False] * ((n - 1 - i*i) // i + 1)
                
        return primes

    def insertNum(self, numstr:str, index:int, newchar:str):
        newstr = ""
        for i in range(len(numstr)):
            newstr += numstr[i] if i != index else newchar
        return int(newstr)

    def minOperations(self, n: int, m: int) -> int:
        primes:List[bool] = self.getPrimes()
        if primes[n]:
            return -1

        def getChildren(num:int):
            numstr = str(num)
            sol = []
            for i in range(len(numstr)):
                digit = int(numstr[i])
                if digit > 0 and not (i == 0 and digit == 1):
                    sol.append(self.insertNum(numstr, i, str(digit - 1)))
                if digit < 9:
                    sol.append(self.insertNum(numstr, i, str(digit + 1)))
            return sol

        heap = []
        heap.append((n, n))
        visited = set()
        while heap:
            (cost, num) = heapq.heappop(heap)
            if num == m:
                return cost
            if num in visited:
                continue
            visited.add(num)
            for child in getChildren(num):
                if not primes[child]:
                    heapq.heappush(heap, (child + cost, child))
        return -1