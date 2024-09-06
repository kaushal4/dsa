class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if len(box) < 1:
            return [[]]

        input_cols = len(box[0])
        sol_box = [[] for _ in range(input_cols)]

        for i in range(len(box)):
            for j in range (len(box[i])-2, -1, -1):
                key = box[i][j]
                if key != "#":
                    continue
                k = j + 1
                while k < len(box[i]) and box[i][k] == ".":
                    box[i][k-1] = box[i][k]
                    k += 1
                box[i][k-1] = key

        for row in box[::-1]:
            for (index, c) in enumerate(row):
                sol_box[index].append(c)
            
        return sol_box