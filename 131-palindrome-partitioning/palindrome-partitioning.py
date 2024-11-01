class Solution:
    def isPali(self, s:str) -> bool:
        n = len(s)
        low = floor((n-1)/2)
        high = ceil((n-1)/2)
        while low >=0 and high < n:
            if s[low] == s[high]:
                low -= 1
                high += 1
            else:
                return False
        return True

    def recur(self, s:str, index:int, cur_array:List[str]):
        if index >= len(s):
            return [cur_array.copy()]
        cur_str = ""
        sol = []
        for i in range(index, len(s)):
            cur_str += s[i]
            if(self.isPali(cur_str)):
                cur_array.append(cur_str)
                sol.extend(self.recur(s, i + 1, cur_array))
                cur_array.pop()
        return sol
        

        
    def partition(self, s: str) -> List[List[str]]:
        return self.recur(s, 0, [])