class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        sor_arr = arr.copy()
        sor_arr.sort()
        num_chunks = 0
        num_freqs_arr = defaultdict(lambda: 0)
        num_freqs_sor = defaultdict(lambda: 0)
        diff = set()
        for i in range(n):
            num_freqs_arr[arr[i]] += 1
            num_freqs_sor[sor_arr[i]] += 1

            if num_freqs_arr[arr[i]] == num_freqs_sor[arr[i]]:
                if arr[i] in diff:
                    diff.remove(arr[i])
            else:
                diff.add(arr[i])

            if num_freqs_arr[sor_arr[i]] == num_freqs_sor[sor_arr[i]]:
                if sor_arr[i] in diff:
                    diff.remove(sor_arr[i])
            else:
                diff.add(sor_arr[i])
            
            if len(diff) == 0:
                num_chunks += 1


        return num_chunks

