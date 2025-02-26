class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        t = len(s3)
        if n + m != t:
            return False
        @cache
        def recur(i: int, j:int):
            if i == -1 and j == -1:
                return True
            canForm = False
            canForm = canForm or (i != -1 and s1[i] == s3[i+j +1] and recur(i-1, j))
            canForm = canForm or (j != -1 and s2[j] == s3[i+j +1] and recur(i, j-1))
            return canForm

        return recur(n-1, m-1)