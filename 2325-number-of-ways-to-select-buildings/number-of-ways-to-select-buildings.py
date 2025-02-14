class Solution:
    def numberOfWays(self, s: str) -> int:
        no_0 = 0
        no_1 = 0
        no_01 = 0
        no_10 = 0
        no_101 = 0
        no_010 = 0

        for c in s:
            if c == '0':
                no_0 = no_0 + 1
                no_10 += no_1
                no_010 += no_01
            else:
                no_1 = no_1 + 1
                no_01 += no_0
                no_101 += no_10
        return no_101 + no_010

        