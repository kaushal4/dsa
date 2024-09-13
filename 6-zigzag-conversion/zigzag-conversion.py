class Solution:
    def getCol(self, numRows, col):
        if col == 0:
            return 0
        return ((numRows + (numRows - 2)) * col)

    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if n == 1 or numRows == 1:
            return s
        sol = ""

        # first row
        col = 0
        while True:
            num = self.getCol(numRows, col)
            if num >= n:
                break
            sol += s[num]
            col+=1
        
        print(sol)

        
        # all middle rows

        for i in range (1, numRows - 1):
            col = 0
            while True:
                num = self.getCol(numRows, col)
                num = num + i
                if num >= n:
                    break
                sol += s[num]
                dif_val = (numRows - 1 - i)
                num = num + dif_val + (dif_val - 1) + 1
                if num >= n:
                    break
                sol += s[num]
                col += 1

        # last row
        col = 0
        while True:
            num = self.getCol(numRows, col)
            num += (numRows - 1)
            if num >= n:
                break
            sol += s[num]
            col+=1
    
        return sol
