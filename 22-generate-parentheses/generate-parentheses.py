class Solution:
    def __init__(self):
        self.sol = []

    def recur(self, n, num_open, cur_string):
        if n == 0 and num_open == 0:
            self.sol.append(cur_string)
        if n != 0:
            s = cur_string + '('
            self.recur(n-1, num_open + 1, s)
        if num_open != 0:
            s = cur_string + ')'
            self.recur(n, num_open - 1, s)

    def generateParenthesis(self, n: int) -> List[str]:
        self.recur(n, 0, "")
        return self.sol