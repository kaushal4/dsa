class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = [['.'] * n for _ in range(n)]

        def checkpos(index:int, pos:int):
            diff = 0
            for i in range(index-1, -1, -1):
                diff += 1
                if pos - diff >= 0 and arr[i][pos - diff] == 'Q':
                    return False
                if pos + diff < n and arr[i][pos+diff] == 'Q':
                    return False
                if arr[i][pos] == 'Q':
                    return False
            return True

        def recur(index:int = 0):
            if index >= n:
                sol = []
                for i in range(n):
                    cur_str = ''
                    for j in range(n):
                        cur_str += arr[i][j]
                    sol.append(cur_str)
                return [sol]

            sol = []
            for i in range(n):
                if checkpos(index, i):
                    arr[index][i] = 'Q'
                    sol.extend(recur(index+1))
                    arr[index][i] = '.'
            return sol

        return recur()