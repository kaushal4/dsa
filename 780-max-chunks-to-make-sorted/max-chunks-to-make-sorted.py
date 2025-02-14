class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        index_sum = 0
        arr_hash = [0] * n
        num_chunks = 0

        for i in range(n):
            num = arr[i]
            arr_hash[num] = 1
            index_sum += arr_hash[i]
            if num < i:
                index_sum += 1

            if index_sum == (i+1):
                num_chunks += 1
        
        return num_chunks