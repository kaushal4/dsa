class TrieNode:
    def __init__(self):
        self.children:Dict[str,TrieNode] = dict()
        self.isLast = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word:str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        print(c)
        node.isLast = True

class Solution:
    def __init__(self):
        self.dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.sol = []

    def isValid(self, x, y, board):
        m = len(board)
        n = len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        return True

    def dfs(self, visited:Set[Tuple[int,int]], board:List[List[str]], cur_cell, node:TrieNode, cur_path):
        m = len(board)
        n = len(board[0])
        x = cur_cell[0]
        y = cur_cell[1]

        if x < 0 or x >= m or y < 0 or y >= n:
            return False

        if cur_cell in visited:
            return False

        if node.isLast:
            self.sol.append(cur_path)
            node.isLast = False

        visited.add(cur_cell)

        for (cx,cy) in self.dir:
            if self.isValid(x+cx, y + cy, board) and (board[x+cx][y+cy] in node.children):
                self.dfs(visited, board, (x + cx, y + cy), node.children[board[x+cx][y+cy]], cur_path + board[x+cx][y+cy])

        visited.remove(cur_cell)


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        trie:Trie = Trie()
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                visited = set()
                if board[i][j] in trie.root.children:
                    self.dfs(visited, board, (i, j), trie.root.children[board[i][j]], board[i][j])
        return self.sol