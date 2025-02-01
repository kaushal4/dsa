class Solution:
    def get_next(self, hash:Dict[str, int]) -> Tuple[str, str]:
        highest = 'A'
        highest_num = 0
        second_highest = 'A'
        second_highest_num = 0
        for key in hash.keys():
            if hash[key] > highest_num:
                highest = key
                highest_num = hash[key]
        for key in hash.keys():
            if hash[key] > second_highest_num and key != highest:
                second_highest = key
                second_highest_num = hash[key]
        return (highest, second_highest)

    def reorganizeString(self, s: str) -> str:
        hash:Dict[str, int] = {chr(c):0 for c in range(97, 97+26)}
        for c in s:
            hash[c] += 1
        
        new_str = ['A']
        start_len = 0
        end_len = 1
        while(start_len != end_len):
            (highest, second_highest) = self.get_next(hash)
            if highest == 'A': break
            if second_highest == 'A' and highest == new_str[-1]:
                print(highest, second_highest, hash, new_str)
                return ""
            hash[highest] -= 1
            if not second_highest == 'A' : hash[second_highest] -= 1
            new_str.append(highest)
            if not second_highest == 'A' : new_str.append(second_highest)
        new_str.pop(0)
        return ''.join(new_str)