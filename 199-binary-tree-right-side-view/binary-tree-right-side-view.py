# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return None
        queue = deque()
        queue.append(root)
        sol = [root.val]
        while queue:
            n = len(queue)
            while n > 0:
                node = queue.popleft()
                if (node.left != None):
                    queue.append(node.left)
                if (node.right != None):
                    queue.append(node.right)
                n -= 1
            if queue:
                sol.append(queue[-1].val)
        return sol