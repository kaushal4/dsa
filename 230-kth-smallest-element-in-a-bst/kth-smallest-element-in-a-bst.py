# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.processed = 0
        self.sol = -1
        self.k = 0

    def inorder(self, root:Optional[TreeNode]): 
        if root == None:
            return
        
        self.inorder(root.left)
        self.processed += 1
        if self.processed == self.k:
            self.sol = root.val
            return
        self.inorder(root.right)
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.inorder(root)
        return self.sol