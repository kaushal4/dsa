class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hash:Dict[int] = dict()
        elements:Set[int] = set()
        for num in nums:
            elements.add(num)
            if num in freq_hash:
                freq_hash[num]+= 1
            else:
                freq_hash[num] = 1
            
        elements:List[int] = list(elements)
        
        def comparator(a, b):
            return 1 if freq_hash[a] < freq_hash[b] else -1

        elements.sort(key=cmp_to_key(comparator))

        return elements[:k]