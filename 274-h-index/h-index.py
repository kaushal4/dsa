class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_val = max(citations)
        n = len(citations)
        best = 0
        for i in range(max_val+1
        ):
            pos = bisect.bisect_left(citations, i)
            if(n - pos >= i):
                best =  i
        return best