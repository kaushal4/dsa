# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root == None:
            return []
        queue.append(root)
        sol = []

        while queue:
            n = len(queue)
            level = []
            while n:
                node = queue.popleft()
                level.append(node.val)
                n -= 1
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            sol.append(level)
            
        return sol



        