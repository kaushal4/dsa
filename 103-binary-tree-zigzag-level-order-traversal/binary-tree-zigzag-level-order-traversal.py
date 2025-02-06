class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []

        if root == None:
            return sol

        q:Deque[TreeNode] = deque()
        q.append(root)
        sol.append([root.val])
        reverse = True

        while q:
            level_size = len(q)
            level = []
            while(level_size):
                level_size -= 1
                node = q.popleft()
                if node.left: 
                    level.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    q.append(node.right)
            if level:
                if reverse:
                    level.reverse()
                    sol.append(level)
                else:
                    sol.append(level)
            reverse = not reverse
        
        return sol

        
        