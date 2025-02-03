class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s) 
        ones = len([x for x in s if x == '1'])
        zeros = len([x for x in s if x == '0'])
        if abs(ones - zeros) > 1:
            return -1
         
        diff1 = 0
        diff2 = 0
 
        for i in range(n):
            if i % 2 == 0 and s[i] == '0':
                  diff1 += 1
            if i % 2 != 0 and s[i] == '1':
                diff1 += 1
            if i % 2 == 0 and s[i] == '1':
                diff2 += 1
            if i % 2 != 0 and s[i] == '0':
                diff2 += 1
        
        if ones < zeros:
            return diff2 // 2
        if zeros < ones:
            return diff1 //2
        
        return min(diff1, diff2) // 2
        