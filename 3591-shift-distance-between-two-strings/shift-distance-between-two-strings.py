class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        def getprev(char:str):
            num = ord(char)
            if num == 97:
                return 'z'
            return chr(num - 1)
        def getNext(char):
            num = ord(char)
            if num == 122:
                return 'a'
            return chr(num + 1)
            
        def forward(a:str, b:str):
            cost = 0
            while a != b:
                cost += nextCost[ord(a) - 97]
                a = getNext(a)
            return cost

        def back(a:str, b:str):
            cost = 0
            while a != b:
                cost += previousCost[ord(a) - 97]
                a = getprev(a)
            return cost
        
        cost = 0
        for i in range(len(s)):
            cost += min(forward(s[i], t[i]), back(s[i], t[i]))
        
        return cost