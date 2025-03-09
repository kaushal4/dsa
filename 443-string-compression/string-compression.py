class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        low = 0
        high = 0
        cur_char = None
        count = 0
        while(high < n):
            if cur_char == None:
                cur_char = chars[high]
                count = 1
                high += 1
            else:
                if cur_char != chars[high]:
                    chars[low] = cur_char
                    low += 1
                    cur_char = None
                    if count == 1: continue
                    count_str = str(count)
                    for ch in count_str:
                        chars[low] = ch
                        low += 1
                else:
                    count += 1
                    high += 1
        if cur_char != None:
            chars[low] = cur_char
            low += 1
            if count > 1: 
                count_str = str(count)
                for ch in count_str:
                    chars[low] = ch
                    low += 1
        return low