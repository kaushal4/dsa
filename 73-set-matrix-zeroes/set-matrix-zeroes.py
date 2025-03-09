class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columnns = set()
        rows = set()
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    columnns.add(j)
                    rows.add(i)
        
        for i in range(n):
            for j in range(m):
                if i in rows or j in columnns:
                    matrix[i][j] = 0