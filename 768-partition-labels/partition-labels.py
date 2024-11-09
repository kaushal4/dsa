class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        largest_number = [0] * 26
        n = len(s)
        for i in range(n):
            largest_number[ord(s[i]) - 97] = i 
        must_include = 0
        i = 0
        sol = []
        while i < n:
            j = i
            while j <= must_include:
                must_include = max(largest_number[ord(s[j]) - 97], must_include)
                j+=1
            sol.append(j - i)
            i = j
            must_include += 1
        return sol