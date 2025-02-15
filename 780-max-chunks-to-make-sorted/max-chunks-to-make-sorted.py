class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        num_max = arr[0]
        num_chunk = 0
        if num_max == 0:
            num_chunk += 1

        for i in range(1, n):
            num = arr[i]
            num_max = max(num, num_max)

            if num_max == i:
                num_chunk += 1
        
        return num_chunk