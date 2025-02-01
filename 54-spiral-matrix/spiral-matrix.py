class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        low_x = 0
        low_y = 0
        high_x = m
        high_y = n
        sol:List[int] = list()

        while(low_x < high_x and low_y < high_y):
            j = low_y 
            i = low_x

            while (j < high_y):
                sol.append(matrix[i][j])
                j +=1 
            j-=1
            i+=1
            low_x += 1

            while(i < high_x):
                sol.append(matrix[i][j])
                i+=1
            i-=1
            j-=1
            high_y -= 1

            if(i == low_x-1):break

            while(j >= low_y):
                sol.append(matrix[i][j])
                j-=1
            j += 1 
            i -= 1
            high_x -= 1

            if(j == high_y):break
            

            while(i >= low_x):
                sol.append(matrix[i][j])
                i-=1
            low_y += 1

        return sol