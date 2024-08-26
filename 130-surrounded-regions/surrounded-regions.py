class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m:int = len(board)
        n:int = len(board[0])
        queue:Deque[Tuple[int]] = deque()

        def addCell(i:int, j:int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] == 'O':
                board[i][j] = 'K'
                queue.append((i,j))
        
        for i in [0,m-1]:
            for j in range(n):
                if board[i][j] == 'O':
                    addCell(i,j)

        for j in [0,n-1]:
            for i in range(m):
                if board[i][j] == 'O':
                    addCell(i,j)

        while queue:
            (x,y) = queue.popleft()
            addCell(x+1, y)
            addCell(x, y+1)
            addCell(x-1, y)
            addCell(x, y-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'K':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'