# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        if root == None:
            return 0
        stack.append((root, root.val))
        sol = 0

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                sol += 1
            if node.left != None:
                stack.append((node.left, max(max_val, node.left.val)))
            if node.right != None:
                stack.append((node.right, max(max_val, node.right.val)))
        
        return sol