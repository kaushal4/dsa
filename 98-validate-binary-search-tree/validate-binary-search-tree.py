# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol = True

    def recurse(self, root:Optional[TreeNode], minimum , maximum):
        if root == None:
            return
        if root.val <= minimum or root.val >= maximum:
            self.sol = False
            return
        self.recurse(root.left, minimum , min(root.val, maximum))
        self.recurse(root.right, max(root.val, minimum), maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return
        self.recurse(root, float('-inf'), float('inf'))
        return self.sol