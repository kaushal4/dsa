class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_hash = [0] * 3
        triplet_index = [0,1,2] 
        for triplet in triplets:
            skip_triplet = False
            for i in triplet_index:
                if triplet[i] > target[i]:
                    skip_triplet = True
                    break
            if skip_triplet:
                continue

            for i in triplet_index:
                if triplet[i] == target[i]:
                    target_hash[i] = 1
        return sum(target_hash) == 3