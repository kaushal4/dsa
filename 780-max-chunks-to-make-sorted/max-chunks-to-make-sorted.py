class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        num_max = -1
        num_chunk = 0

        for i in range(n):
            num = arr[i]
            num_max = max(num, num_max)

            if num_max == i:
                num_chunk += 1
        
        return num_chunk