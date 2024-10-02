class Solution:
    def notValid(self,arr):
        s = set()
        for ar in arr:
            if ar in s:
                return True
            s.add(ar)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            arr = []
            for j in range(0,9):
                if board[i][j] != ".":
                    arr.append(int(board[i][j]))
            if self.notValid(arr):
                return False
        
        for i in range(0,9):
            arr = []
            for j in range(0,9):
                if board[j][i] != ".":
                    arr.append(int(board[j][i]))
            if self.notValid(arr):
                return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                arr = []
                for k in range(i,i+3):
                    for l in range(j, j+3):
                        if board[k][l] != ".":
                            arr.append(int(board[k][l]))
                if self.notValid(arr):
                    return False
        return True



        


        